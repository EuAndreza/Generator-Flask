from flask import make_response
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import date

data = date.today()


def pdf(
		nome, estado_civil, profissao, cpf, rg, rua, bairro, municipio, estado, cep, fone, nome_pro, estado_civil_pro,
		profissao_pro, cpf_pro, rg_pro, rua_pro, municipio_pro, bairro_pro, estado_pro, cep_pro, fone_pro, texto
):
	mes = ''
	output = BytesIO()

	gerador = canvas.Canvas(output)
	gerador.setFont('Helvetica', 12)
	gerador.drawImage('brasao.jpeg', 260, 745)
			
	# ajusta texto para a solicitação
	text = texto.split()
	text_line1 = text[:7]
	text_line2 = text[7:22]
	text_line3 = text[22:38]
	text_line4 = text[38:43]

	# ajusta nome de profissão
	prof = profissao.split()
	prof_line1 = prof[0:]
	prof_line2 = prof[1:]

	# converter o mes de numero para texto
	if data.month == 1:
		mes = 'janeiro'
	elif data.month == 2:
		mes = 'fevereiro'
	elif data.month == 3:
		mes = 'março'
	elif data.month == 4:
		mes = 'abril'
	elif data.month == 5:
		mes = 'maio'
	elif data.month == 6:
		mes = 'junho'
	elif data.month == 7:
		mes = 'julho'
	elif data.month == 8:
		mes = 'agosto'
	elif data.month == 9:
		mes = 'setembro'
	elif data.month == 10:
		mes = 'outubro'
	elif data.month == 11:
		mes = 'novembro'
	elif data.month == 12:
		mes = 'dezembro'
	# titulo
	gerador.drawString(200, 730, 'PROCURAÇÃO - PESSOA FÍSICA')

	# linha 1
	gerador.drawString(30, 700, 'ORTOGANTE: ')
	gerador.line(115, 700, 310, 700)
	# adiciona o nome do pdf
	gerador.drawString(120, 703, nome)
	gerador.drawString(311, 700, ', brasileiro(a),')
	gerador.line(385, 700, 480, 700)
	# adiciona o estado civil no pdf
	gerador.drawString(390, 703, estado_civil)
	gerador.line(485, 700, 580, 700)
	# adiciona a profissao no pdf
	gerador.drawString(490, 703, ' '.join(prof_line1))
	# linha 2
	gerador.line(30, 670, 200, 670)
	gerador.drawString(35, 673, ' '.join(prof_line2))
	gerador.drawString(201, 670, ', portador(a) do CPF n°')
	gerador.line(330, 670, 435, 670)
	# adiciona o cpf no pdf
	gerador.drawString(340, 673, cpf)
	gerador.drawString(436, 670, ', RG n°')
	gerador.line(480, 670, 580, 670)
	# adiciona o rg no pdf
	gerador.drawString(490, 673, rg)
	# linha 3
	gerador.drawString(30, 640, 'residente e domiciliado(a) na (rua, avenida, etc)')
	gerador.line(290, 640, 530, 640)
	# adiciona a rua no pdf
	gerador.drawString(300, 643, rua)
	gerador.drawString(531, 640, ', (bairro)')
	# linha 4
	gerador.line(30, 610, 190, 610)
	# adiciona bairro no pdf
	gerador.drawString(35, 613, bairro)
	gerador.drawString(191, 610, ', municipio')
	gerador.line(250, 610, 430, 610)
	# adiciona municipio no pdf
	gerador.drawString(260, 613, municipio)
	gerador.drawString(431, 610, ', estado')
	gerador.line(480, 610, 580, 610)
	# adiciona estado no pdf
	gerador.drawString(490, 613, estado)
	# linha 5
	gerador.drawString(30, 580, 'CEP')
	gerador.line(60, 580, 190, 580)
	# adiciona cep no pdf
	gerador.drawString(70, 583, cep)
	gerador.drawString(191, 580, ', telefone')
	gerador.line(245, 580, 390, 580)
	# adiciona telefone em pdf
	gerador.drawString(255, 583, fone)
	gerador.drawString(391, 580, ', pelo presente instrumento nomeia')
	# linha 6
	gerador.drawString(30, 550, 'e constitui como seu(sua) bastante Procurador(a) (Outorgado)')
	gerador.line(365, 550, 580, 550)
	# adiciona nome de procurador no pdf
	gerador.drawString(375, 553, nome_pro)
	# linha 7
	gerador.drawString(30, 520, 'brasileiro(a),')
	gerador.line(100, 520, 195, 520)
	# adiciona estado civil do procurador no pdf
	gerador.drawString(110, 523, estado_civil_pro)
	gerador.line(200, 520, 450, 520)
	# adiciona profissão do procurador no pdf
	gerador.drawString(210, 523, profissao_pro)
	gerador.drawString(451, 520, ', portador(a) do CPF n°')
	# linha 8
	gerador.line(30, 490, 150, 490)
	# adiciona cpf do procurador no pdf
	gerador.drawString(40, 493, cpf_pro)
	gerador.drawString(151, 490, ', RG n°')
	gerador.line(195, 490, 315, 490)
	# adiciona rg do procurador no pdf
	gerador.drawString(205, 493, rg_pro)
	gerador.drawString(316, 490, ', residente e domiciliado(a) na (rua, avenida, etc)')
	# linha 9
	gerador.line(30, 460, 270, 460)
	# adiciona rua do procurador no pdf
	gerador.drawString(40, 463, rua_pro)
	gerador.drawString(271, 460, ', (bairro)')
	gerador.line(320, 460, 515, 460)
	# adiciona bairro do procurador no pdf
	gerador.drawString(330, 463, bairro_pro)
	gerador.drawString(516, 460, ', municipio')
	# linha 10
	gerador.line(30, 430, 150, 430)
	# adiciona municipio do procurador no pdf
	gerador.drawString(40, 433, municipio_pro)
	gerador.drawString(151, 430, ', estado')
	gerador.line(200, 430, 330, 430)
	# adiciona estado do procurador no pdf
	gerador.drawString(210, 433, estado_pro)
	gerador.drawString(331, 430, ', CEP')
	gerador.line(370, 430, 525, 430)
	# adiciona cep do procurador no pdf
	gerador.drawString(380, 433, cep_pro)
	gerador.drawString(526, 430, ', telefone')
	# linha 11
	gerador.line(30, 400, 200, 400)
	# adiciona telefone do procurador no pdf
	gerador.drawString(40, 403, fone_pro)
	gerador.drawString(201, 400, ', com poderes para representar o outorgante perante (todos os orgãos')
	# linha 12
	gerador.drawString(
		30, 370, 'da administração pública Federal, Estadual,  Distrital e  Municipal,  inclusive perante)  às  '
		'Unidades  da'
	)
	# linha 13
	gerador.drawString(30, 340, 'Receita Federal do Brasil para requerer/solicitar ')
	gerador.line(290, 340, 580, 340)
	gerador.drawString(300, 343, ' '.join(text_line1))
	# linha 14
	gerador.line(30, 310, 580, 310)
	gerador.drawString(40, 313, ' '.join(text_line2))
	# linha 15
	gerador.line(30, 280, 580, 280)
	gerador.drawString(40, 283, ' '.join(text_line3))
	# linha 16
	gerador.line(30, 250, 280, 250)
	gerador.drawString(40, 253, ' '.join(text_line4))
	gerador.drawString(281, 250, ',  responsabilizando-se por todos os atos  praticados no')
	# linha 17
	gerador.drawString(
		30, 220, 'cumprimento deste instrumento,  cessando  os  efeitos  deste  a  partir  da(o) (extinção do seu '
		'objetivo)'
	)
	# linha 18
	gerador.drawString(30, 190, '(dia/mês/ano).')
	# linha 19
	gerador.line(100, 130, 250, 130)
	gerador.drawString(120, 133, municipio)
	gerador.line(255, 130, 310, 130)
	gerador.drawString(265, 133, str(data.day))
	gerador.drawString(312, 130, 'de')
	gerador.line(330, 130, 430, 130)
	gerador.drawString(340, 133, mes)
	gerador.drawString(432, 130, 'de')
	gerador.line(450, 130, 505, 130)
	gerador.drawString(460, 133, str(data.year))
	# linha 20
	gerador.line(100, 100, 505, 100)
	gerador.drawString(240, 85, '(Assinatura do Outorgante)')

	gerador.showPage()
	gerador.save()
	
	pdf_out = output.getvalue()
	output.close()

	response = make_response(pdf_out)
	response.headers['Content-Disposition'] = "attachment; filename={}.pdf".format(nome)
	response.mimetype = 'application/pdf'
	return response
