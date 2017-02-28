# -*- coding: utf-8 -*-
    
from openerp import models, fields, api
from datetime import date, datetime

class Persona(models.Model):
    _name = 'hospital.persona'
    
    name = fields.Char(string="Nombre", required=True)


class Medico(models.Model):
    _name = 'hospital.medico'
    _inherit = 'hospital.persona'
    
    especialidad = fields.Many2one('hospital.especialidad', required=True)
    """
    anyo_licen = fields.Date()
    anyos_experiencia = fields.Char()
    
    @api.onchange('anyo_licen')
    def _calc_exp(self):
        for r in self:
            if r.anyo_licen:
                dt = r.anyo_licen
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = d2 - d1
                rd_years = rd.strftime("%Y")
                r.anyos_experiencia = rd_years
    """
    
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
    
