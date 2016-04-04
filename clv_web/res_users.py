# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

import logging
from openerp import models, fields

from openerp import SUPERUSER_ID

_logger = logging.getLogger(__name__)


class res_users(models.Model):
    _inherit = 'res.users'

    disable_web_access = fields.Boolean('Disable Web Access', help="Check to disable user web access.",
                                        default=False)

    def authenticate(self, db, login, password, user_agent_env):
        """Verifies and returns the user ID corresponding to the given
          ``login`` and ``password`` combination, or False if there was
          no matching user.

           :param str db: the database on which user is trying to authenticate
           :param str login: username
           :param str password: user password
           :param dict user_agent_env: environment dictionary describing any
               relevant environment attributes
        """

        uid = self._login(db, login, password)

        cr = self.pool.cursor()
        try:
            cr.execute('SELECT disable_web_access FROM res_users WHERE id=%s', (uid,))
            if cr.rowcount:
                disable_web_access = cr.fetchone()[0]
                if disable_web_access is True:
                    return 0
        except Exception:
            _logger.exception("Failed to verify disable_web_access configuration parameter")
        finally:
            cr.close()

        if uid == SUPERUSER_ID:
            # Successfully logged in as admin!
            # Attempt to guess the web base url...
            if user_agent_env and user_agent_env.get('base_location'):
                cr = self.pool.cursor()
                try:
                    base = user_agent_env['base_location']
                    ICP = self.pool['ir.config_parameter']
                    if not ICP.get_param(cr, uid, 'web.base.url.freeze'):
                        ICP.set_param(cr, uid, 'web.base.url', base)
                    cr.commit()
                except Exception:
                    _logger.exception("Failed to update web.base.url configuration parameter")
                finally:
                    cr.close()
        return uid
