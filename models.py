# -*- coding: utf-8 -*-
    
from openerp import models, fields

class Medico(models.Model):
    _name = 'hospital.medico'
    
    name = fields.Char(string="Nombre", required=True)
    especialidad = fields.Many2one('hospital.especialidad', required=True)
                         
class Especialidad(models.Model):
    _name = 'especialidad'
    
    name = fields.Char(string="Nombre", required=True)
        
class Consulta(models.Model):
    _name = 'consulta'
    
    name = fields.Char(string="Nombre", required=True)
    
    partner_id = fields.Many2one('res.partner', string="Paciente")
    especialidades = fields.Many2one('especialidad',
        ondelete='cascade', string="Especialidad", required=True)