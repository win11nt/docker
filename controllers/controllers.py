# -*- coding: utf-8 -*-
# from odoo import http


# class TutorialSnippets(http.Controller):
#     @http.route('/tutorial_snippets/tutorial_snippets', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_snippets/tutorial_snippets/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_snippets.listing', {
#             'root': '/tutorial_snippets/tutorial_snippets',
#             'objects': http.request.env['tutorial_snippets.tutorial_snippets'].search([]),
#         })

#     @http.route('/tutorial_snippets/tutorial_snippets/objects/<model("tutorial_snippets.tutorial_snippets"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_snippets.object', {
#             'object': obj
#         })
