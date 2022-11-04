from django.core.management.base import BaseCommand #, CommandError
from django.utils.dateparse import parse_datetime
import os
import csv
from django.conf import settings
from datetime import datetime
from juri.models import Casacion, Sala

class Command(BaseCommand):
	help = 'Importa casaciones usando un archivo casacion.csv en la ruta del projecto'
	def handle(self, *args, **options):
		print('in command')
		with open(os.path.join(settings.BASE_DIR / 'casacion.csv'), 'r') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			#for row in csv_reader:
			for index, row in enumerate(csv_reader, start=1):
				val_4 = None
				if row[4]:
					sala = Sala.objects.get(id=int(row[4]))
					val_4 = sala
				val_7 = None
				if row[7]:
					val_7 = int(row[7])
				val_10 = None
				if row[10]:
					val_10 = int(row[10])
				val_14 = None
				if row[14]:
					val_14 = row[14].split(',')
					#for i in val_14:
					#	print(i.strip())
				val_17 = None
				if row[17]:
					val_17 = parse_datetime(row[17])
				val_18 = None
				if row[18]:
					val_18 = parse_datetime(row[18])
				print(f'========{index}=========')
				print(f'in row0: {row[0]}')
				print(f'in row1: {row[1]}')
				print(f'in row2: {row[2]}')
				print(f'in row3: {row[3]}')
				print(f'in row4: {val_4}')
				print(f'in row5: {row[5]}')
				print(f'in row6: {row[6]}')
				print(f'in row7: {val_7}')
				print(f'in row8: {row[8]}')
				print(f'in row9: {row[9]}')
				print(f'in row10: {val_10}')
				print(f'in row11: {row[11]}')
				print(f'in row12: {row[12]}')
				print(f'in row13: {row[13]}')
				print(f'in row14: {val_14}')
				print(f'in row15: {row[15]}')
				print(f'in row16: {row[16]}')
				print(f'in row17: {val_17}')
				print(f'in row18: {val_18}')
				print(f'in row19: {row[19]}')
				#"""
				casacion = Casacion(
					numero=row[0], 
					materia=row[1], 
					sumilla=row[2],
					extracto=row[3], 
					sala=val_4,
					demandante=row[5],
					demandado=row[6], 
					parte=val_7,
					casante=row[8],
					es_precedente=row[9], 
					fallo=val_10,  
					juezponente_nombre=row[11],
					jueces_nombres=row[12],
					juezdiscordia_nombre=row[13],
					boletin=row[15],
					pagina=row[16],
					fecha_inicio=val_17,
					fecha_sentencia=val_18,
					texto=row[19]
					)
				casacion.save()
				print(f'saved casacion: {casacion.numero}')
				if row[14]:
					print(f'row_14: {row[14]}')
					areas = [int(i) for i in row[14].split(',') if i.strip().isdigit()]
					print(f'areas: {areas}')
					for i in areas:
						casacion.area.add(i)
				#"""

		