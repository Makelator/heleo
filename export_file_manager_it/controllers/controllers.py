# -*- coding: utf-8 -*-
import base64
import odoo.http as http
from odoo.http import request

class Controller(http.Controller):
	@http.route(['/download/file/<model("export.file.manager"):obj>'],type='http',auth='public')
	def render_file(self,obj,**kw):
		if obj.exists():
			file = base64.b64decode(obj.file)
			headers = [
				('Content-Length', len(file)),
				('Content-Disposition', u'attachment; filename="%s"'%obj.file_name),
			]
			if obj.content_type:
				headers.append(('Content-Type',obj.content_type))
			return request.make_response(file, headers=headers)