# -*- coding: utf-8 -*-
    
from openerp import models, fields, api

class Persona(models.Model):
    _name = 'hospital.persona'
    
    name = fields.Char(string="Nombre", required=True)


class Medico(models.Model):
    _name = 'hospital.medico'
    _inherit = 'hospital.persona'
    
    especialidad = fields.Many2one('hospital.especialidad', required=True)
    nivel = fields.Integer()
    experiencia = fields.Integer()
    sanacion = fields.Integer(compute='_calc_san')
    
    @api.depends('nivel', 'experiencia')
    def _calc_san(self):
        for r in self:
            r.sanacion = r.nivel * r.experiencia
            
    
class Paciente(models.Model):
    _name = 'hospital.paciente'
    _inherit = 'hospital.persona'
                         
class Especialidad(models.Model):
    _name = 'hospital.especialidad'
    
    name = fields.Char(string="Nombre", required=True)
        
class Consulta(models.Model):
    _name = 'hospital.consulta'
    
    name = fields.Char(string="Nombre", required=True)
    
    paciente_id = fields.Many2one('hospital.paciente', string="Paciente")
    especialidad = fields.Many2one('hospital.especialidad',
        ondelete='cascade', string="Especialidad", required=True)
    
