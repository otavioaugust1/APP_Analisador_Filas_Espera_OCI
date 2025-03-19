# Bibliotecas
import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox

import pandas as pd
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas

# Definição dos agrupamentos
agrupamentos = {
    '0901010014': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA INICIAL DE CÂNCER DE MAMA',
        'itens_obrigatorios': [
            {'codigo': '0204030030', 'descricao': 'MAMOGRAFIA'},
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0205020097',
                'descricao': 'ULTRASSONOGRAFIA MAMARIA BILATERAL',
            }
        ],
    },
    '0901010090': {
        'nome': 'OCI PROGRESSÃO DA AVALIAÇÃO DIAGNÓSTICA DE CÂNCER DE MAMA - I',
        'itens_obrigatorios': [
            {
                'codigo': '0203010043',
                'descricao': 'EXAME CITOPATOLOGICO DE MAMA',
            },
            {
                'codigo': '0201010585',
                'descricao': 'PUNÇÃO ASPIRATIVA DE MAMA POR AGULHA FINA',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0201010569',
                'descricao': 'BIOPSIA/EXERESE DE NÓDULO DE MAMA',
            }
        ],
    },
    '0901010103': {
        'nome': 'OCI PROGRESSÃO DA AVALIAÇÃO DIAGNÓSTICA DE CÂNCER DE MAMA-II',
        'itens_obrigatorios': [
            {
                'codigo': '0201010607',
                'descricao': 'PUNÇÃO DE MAMA POR AGULHA GROSSA',
            },
            {
                'codigo': '0203020065',
                'descricao': 'EXAME ANATOMOPATOLOGICO DE MAMA - BIOPSIA',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0201010569',
                'descricao': 'BIOPSIA/EXERESE DE NÓDULO DE MAMA',
            }
        ],
    },
    '0901010057': {
        'nome': 'OCI INVESTIGAÇÃO DIAGNÓSTICA DE CÂNCER DE COLO DE ÚTERO',
        'itens_obrigatorios': [
            {'codigo': '0201010666', 'descricao': 'BIOPSIA DO COLO UTERINO'},
            {
                'codigo': '0203020081',
                'descricao': 'EXAME ANATOMO-PATOLOGICO DO COLO UTERINO - BIOPSIA',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0211040029', 'descricao': 'COLPOSCOPIA'}
        ],
    },
    '0901010111': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA E TERAPÊUTICA DE CÂNCER DE COLO DO ÚTERO-I',
        'itens_obrigatorios': [
            {
                'codigo': '0203020022',
                'descricao': 'EXAME ANATOMO-PATOLOGICO DO COLO UTERINO - PECA CIRURGICA',
            },
            {
                'codigo': '0409060089',
                'descricao': 'EXCISÃO TIPO I DO COLO UTERINO',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0211040029', 'descricao': 'COLPOSCOPIA'}
        ],
    },
    '0901010120': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA E TERAPÊUTICA DE CÂNCER DE COLO DO ÚTERO-II',
        'itens_obrigatorios': [
            {
                'codigo': '0203020022',
                'descricao': 'EXAME ANATOMO-PATOLOGICO DO COLO UTERINO - PECA CIRURGICA',
            },
            {
                'codigo': '0409060305',
                'descricao': 'EXCISÃO TIPO 2 DO COLO UTERINO',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0211040029', 'descricao': 'COLPOSCOPIA'}
        ],
    },
    '0901010049': {
        'nome': 'OCI PROGRESSÃO DA AVALIAÇÃO DIAGNÓSTICA DE CÂNCER DE PRÓSTATA',
        'itens_obrigatorios': [
            {'codigo': '0201010410', 'descricao': 'BIÓPSIA DE PRÓSTATA'},
            {
                'codigo': '0203020030',
                'descricao': 'EXAME ANATOMO-PATOLÓGICO PARA CONGELAMENTO / PARAFINA POR PEÇA CIRURGICA OU POR BIOPSIA (EXCETO COLO UTERINO E MAMA)',
            },
            {
                'codigo': '0205020119',
                'descricao': 'ULTRASSONOGRAFIA DE PROSTATA (VIA TRANSRETAL)',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [],
    },
    '0901010073': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA DE CÂNCER GÁSTRICO',
        'itens_obrigatorios': [
            {
                'codigo': '0209010037',
                'descricao': 'ESOFAGOGASTRODUODENOSCOPIA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0203020030',
                'descricao': 'EXAME ANATOMO-PATOLÓGICO PARA CONGELAMENTO / PARAFINA POR PEÇA CIRURGICA OU POR BIOPSIA (EXCETO COLO UTERINO E MAMA)',
            }
        ],
    },
    '0901010081': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA DE CÂNCER COLORRETAL',
        'itens_obrigatorios': [
            {'codigo': '0209010029', 'descricao': 'COLONOSCOPIA (COLOSCOPIA)'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0203020030',
                'descricao': 'EXAME ANATOMO-PATOLÓGICO PARA CONGELAMENTO / PARAFINA POR PEÇA CIRURGICA OU POR BIOPSIA (EXCETO COLO UTERINO E MAMA)',
            }
        ],
    },
    '0902010018': {
        'nome': 'OCI AVALIAÇÃO DE RISCO CIRÚRGICO',
        'itens_obrigatorios': [
            {'codigo': '0211020036', 'descricao': 'ELETROCARDIOGRAMA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0202010279', 'descricao': 'DOSAGEM DE COLESTEROL HDL'},
            {'codigo': '0202010287', 'descricao': 'DOSAGEM DE COLESTEROL LDL'},
            {
                'codigo': '0202010295',
                'descricao': 'DOSAGEM DE COLESTEROL TOTAL',
            },
            {'codigo': '0202010317', 'descricao': 'DOSAGEM DE CREATININA'},
            {'codigo': '0202010473', 'descricao': 'DOSAGEM DE GLICOSE'},
            {
                'codigo': '0202010503',
                'descricao': 'DOSAGEM DE HEMOGLOBINA GLICOSILADA',
            },
            {'codigo': '0202010600', 'descricao': 'DOSAGEM DE POTASSIO'},
            {'codigo': '0202010635', 'descricao': 'DOSAGEM DE SODIO'},
            {
                'codigo': '0202010643',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-OXALACETICA (TGO)',
            },
            {
                'codigo': '0202010651',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-PIRUVICA (TGP)',
            },
            {'codigo': '0202010678', 'descricao': 'DOSAGEM DE TRIGLICERIDEOS'},
            {'codigo': '0202010694', 'descricao': 'DOSAGEM DE UREIA'},
            {'codigo': '0202020380', 'descricao': 'HEMOGRAMA COMPLETO'},
            {
                'codigo': '0204030153',
                'descricao': 'RADIOGRAFIA DE TORAX (PA E PERFIL)',
            },
        ],
    },
    '0902010026': {
        'nome': 'OCI AVALIAÇÃO CARDIOLÓGICA',
        'itens_obrigatorios': [
            {
                'codigo': '0204030153',
                'descricao': 'RADIOGRAFIA DE TORAX (PA E PERFIL)',
            },
            {'codigo': '0211020036', 'descricao': 'ELETROCARDIOGRAMA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0202010279', 'descricao': 'DOSAGEM DE COLESTEROL HDL'},
            {'codigo': '0202010287', 'descricao': 'DOSAGEM DE COLESTEROL LDL'},
            {
                'codigo': '0202010295',
                'descricao': 'DOSAGEM DE COLESTEROL TOTAL',
            },
            {'codigo': '0202010317', 'descricao': 'DOSAGEM DE CREATININA'},
            {'codigo': '0202010473', 'descricao': 'DOSAGEM DE GLICOSE'},
            {
                'codigo': '0202010503',
                'descricao': 'DOSAGEM DE HEMOGLOBINA GLICOSILADA',
            },
            {'codigo': '0202010600', 'descricao': 'DOSAGEM DE POTASSIO'},
            {'codigo': '0202010635', 'descricao': 'DOSAGEM DE SODIO'},
            {
                'codigo': '0202010643',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-OXALACETICA (TGO)',
            },
            {
                'codigo': '0202010651',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-PIRUVICA (TGP)',
            },
            {'codigo': '0202010678', 'descricao': 'DOSAGEM DE TRIGLICERIDEOS'},
            {'codigo': '0202010694', 'descricao': 'DOSAGEM DE UREIA'},
            {'codigo': '0202020380', 'descricao': 'HEMOGRAMA COMPLETO'},
            {
                'codigo': '0205010032',
                'descricao': 'ECOCARDIOGRAFIA TRANSTORACICA',
            },
        ],
    },
    '0902010034': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA INICIAL - SÍNDROME CORONARIANA CRÔNICA',
        'itens_obrigatorios': [
            {'codigo': '0211020036', 'descricao': 'ELETROCARDIOGRAMA'},
            {
                'codigo': '0211020060',
                'descricao': 'TESTE DE ESFORCO / TESTE ERGOMETRICO',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0202010279', 'descricao': 'DOSAGEM DE COLESTEROL HDL'},
            {'codigo': '0202010287', 'descricao': 'DOSAGEM DE COLESTEROL LDL'},
            {
                'codigo': '0202010295',
                'descricao': 'DOSAGEM DE COLESTEROL TOTAL',
            },
            {'codigo': '0202010317', 'descricao': 'DOSAGEM DE CREATININA'},
            {'codigo': '0202010473', 'descricao': 'DOSAGEM DE GLICOSE'},
            {
                'codigo': '0202010503',
                'descricao': 'DOSAGEM DE HEMOGLOBINA GLICOSILADA',
            },
            {'codigo': '0202010600', 'descricao': 'DOSAGEM DE POTASSIO'},
            {'codigo': '0202010635', 'descricao': 'DOSAGEM DE SODIO'},
            {
                'codigo': '0202010643',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-OXALACETICA (TGO)',
            },
            {
                'codigo': '0202010651',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-PIRUVICA (TGP)',
            },
            {'codigo': '0202010678', 'descricao': 'DOSAGEM DE TRIGLICERIDEOS'},
            {'codigo': '0202010694', 'descricao': 'DOSAGEM DE UREIA'},
            {'codigo': '0202020380', 'descricao': 'HEMOGRAMA COMPLETO'},
            {
                'codigo': '0205010032',
                'descricao': 'ECOCARDIOGRAFIA TRANSTORACICA',
            },
        ],
    },
    '0902010042': {
        'nome': 'OCI PROGRESSÃO DA AVALIAÇÃO DIAGNÓSTICA I – SÍNDROME CORONARIANA CRÔNICA',
        'itens_obrigatorios': [
            {
                'codigo': '0205010016',
                'descricao': 'ECOCARDIOGRAFIA DE ESTRESSE',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [],
    },
    '0902010050': {
        'nome': 'OCI PROGRESSÃO DA AVALIAÇÃO DIAGNÓSTICA II – SÍNDROME CORONARIANA CRÔNICA',
        'itens_obrigatorios': [
            {
                'codigo': '0208010025',
                'descricao': 'CINTILOGRAFIA DE MIOCARDIO P/ AVALIACAO DA PERFUSAO EM SITUACAO DE ESTRESSE (MINIMO 3 PROJECOES)',
            },
            {
                'codigo': '0208010033',
                'descricao': 'CINTILOGRAFIA DE MIOCARDIO P/ AVALIACAO DA PERFUSAO EM SITUACAO DE REPOUSO (MINIMO 3 PROJECOES)',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [],
    },
    '0902010069': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA - INSUFICIÊNCIA CARDÍACA',
        'itens_obrigatorios': [
            {
                'codigo': '0202010791',
                'descricao': 'DOSAGEM DE PEPTÍDEOS NATRIURÉTICOS TIPO B (BNP E NT-PROBNP)',
            },
            {'codigo': '0211020036', 'descricao': 'ELETROCARDIOGRAMA'},
            {
                'codigo': '0211020044',
                'descricao': 'MONITORAMENTO PELO SISTEMA HOLTER 24 HS (3 CANAIS)',
            },
            {
                'codigo': '0211020060',
                'descricao': 'TESTE DE ESFORCO / TESTE ERGOMETRICO',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0202010279', 'descricao': 'DOSAGEM DE COLESTEROL HDL'},
            {'codigo': '0202010287', 'descricao': 'DOSAGEM DE COLESTEROL LDL'},
            {
                'codigo': '0202010295',
                'descricao': 'DOSAGEM DE COLESTEROL TOTAL',
            },
            {'codigo': '0202010317', 'descricao': 'DOSAGEM DE CREATININA'},
            {'codigo': '0202010473', 'descricao': 'DOSAGEM DE GLICOSE'},
            {
                'codigo': '0202010503',
                'descricao': 'DOSAGEM DE HEMOGLOBINA GLICOSILADA',
            },
            {'codigo': '0202010600', 'descricao': 'DOSAGEM DE POTASSIO'},
            {'codigo': '0202010635', 'descricao': 'DOSAGEM DE SODIO'},
            {
                'codigo': '0202010643',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-OXALACETICA (TGO)',
            },
            {
                'codigo': '0202010651',
                'descricao': 'DOSAGEM DE TRANSAMINASE GLUTAMICO-PIRUVICA (TGP)',
            },
            {'codigo': '0202010678', 'descricao': 'DOSAGEM DE TRIGLICERIDEOS'},
            {'codigo': '0202010694', 'descricao': 'DOSAGEM DE UREIA'},
            {'codigo': '0202020380', 'descricao': 'HEMOGRAMA COMPLETO'},
            {
                'codigo': '0205010032',
                'descricao': 'ECOCARDIOGRAFIA TRANSTORACICA',
            },
        ],
    },
    '0903010011': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA EM ORTOPEDIA COM RECURSOS DE RADIOLOGIA',
        'itens_obrigatorios': [
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0204020034',
                'descricao': 'RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO + OBLIQUAS)',
            },
            {
                'codigo': '0204020042',
                'descricao': 'RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO / FLEXAO)',
            },
            {
                'codigo': '0204020077',
                'descricao': 'RADIOGRAFIA DE COLUNA LOMBO-SACRA (C/ OBLIQUAS)',
            },
            {
                'codigo': '0204020085',
                'descricao': 'RADIOGRAFIA DE COLUNA LOMBO-SACRA FUNCIONAL / DINAMICA',
            },
            {
                'codigo': '0204020093',
                'descricao': 'RADIOGRAFIA DE COLUNA TORACICA (AP + LATERAL)',
            },
            {
                'codigo': '0204020107',
                'descricao': 'RADIOGRAFIA DE COLUNA TORACO-LOMBAR',
            },
            {
                'codigo': '0204020131',
                'descricao': 'RADIOGRAFIA PANORAMICA DE COLUNA TOTAL- TELESPONDILOGRAFIA ( P/ ESCOLIOSE)',
            },
            {
                'codigo': '0204040035',
                'descricao': 'RADIOGRAFIA DE ARTICULACAO ESCAPULO-UMERAL',
            },
            {'codigo': '0204040078', 'descricao': 'RADIOGRAFIA DE COTOVELO'},
            {'codigo': '0204040094', 'descricao': 'RADIOGRAFIA DE MAO'},
            {
                'codigo': '0204040116',
                'descricao': 'RADIOGRAFIA DE ESCAPULA/OMBRO (TRES POSICOES)',
            },
            {
                'codigo': '0204040124',
                'descricao': 'RADIOGRAFIA DE PUNHO (AP + LATERAL + OBLIQUA)',
            },
            {
                'codigo': '0204060060',
                'descricao': 'RADIOGRAFIA DE ARTICULACAO COXO-FEMORAL',
            },
            {'codigo': '0204060095', 'descricao': 'RADIOGRAFIA DE BACIA'},
            {'codigo': '0204060109', 'descricao': 'RADIOGRAFIA DE CALCANEO'},
            {
                'codigo': '0204060125',
                'descricao': 'RADIOGRAFIA DE JOELHO (AP + LATERAL)',
            },
            {
                'codigo': '0204060133',
                'descricao': 'RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + AXIAL)',
            },
            {
                'codigo': '0204060141',
                'descricao': 'RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + OBLIQUA + 3 AXIAIS)',
            },
            {
                'codigo': '0204060150',
                'descricao': 'RADIOGRAFIA DE PE / DEDOS DO PE',
            },
            {
                'codigo': '0204060176',
                'descricao': 'RADIOGRAFIA PANORAMICA DE MEMBROS INFERIORES',
            },
        ],
    },
    '0903010020': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA EM ORTOPEDIA COM RECURSOS DE RADIOLOGIA E ULTRASSONOGRAFIA',
        'itens_obrigatorios': [
            {
                'codigo': '0205020062',
                'descricao': 'ULTRASSONOGRAFIA DE ARTICULACAO',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0204020034',
                'descricao': 'RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO + OBLIQUAS)',
            },
            {
                'codigo': '0204020042',
                'descricao': 'RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO / FLEXAO)',
            },
            {
                'codigo': '0204020077',
                'descricao': 'RADIOGRAFIA DE COLUNA LOMBO-SACRA (C/ OBLIQUAS)',
            },
            {
                'codigo': '0204020085',
                'descricao': 'RADIOGRAFIA DE COLUNA LOMBO-SACRA FUNCIONAL / DINAMICA',
            },
            {
                'codigo': '0204020093',
                'descricao': 'RADIOGRAFIA DE COLUNA TORACICA (AP + LATERAL)',
            },
            {
                'codigo': '0204020107',
                'descricao': 'RADIOGRAFIA DE COLUNA TORACO-LOMBAR',
            },
            {
                'codigo': '0204020131',
                'descricao': 'RADIOGRAFIA PANORAMICA DE COLUNA TOTAL- TELESPONDILOGRAFIA ( P/ ESCOLIOSE)',
            },
            {
                'codigo': '0204040035',
                'descricao': 'RADIOGRAFIA DE ARTICULACAO ESCAPULO-UMERAL',
            },
            {'codigo': '0204040078', 'descricao': 'RADIOGRAFIA DE COTOVELO'},
            {'codigo': '0204040094', 'descricao': 'RADIOGRAFIA DE MAO'},
            {
                'codigo': '0204040116',
                'descricao': 'RADIOGRAFIA DE ESCAPULA/OMBRO (TRES POSICOES)',
            },
            {
                'codigo': '0204040124',
                'descricao': 'RADIOGRAFIA DE PUNHO (AP + LATERAL + OBLIQUA)',
            },
            {
                'codigo': '0204060060',
                'descricao': 'RADIOGRAFIA DE ARTICULACAO COXO-FEMORAL',
            },
            {'codigo': '0204060095', 'descricao': 'RADIOGRAFIA DE BACIA'},
            {'codigo': '0204060109', 'descricao': 'RADIOGRAFIA DE CALCANEO'},
            {
                'codigo': '0204060125',
                'descricao': 'RADIOGRAFIA DE JOELHO (AP + LATERAL)',
            },
            {
                'codigo': '0204060133',
                'descricao': 'RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + AXIAL)',
            },
            {
                'codigo': '0204060141',
                'descricao': 'RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + OBLIQUA + 3 AXIAIS)',
            },
            {
                'codigo': '0204060150',
                'descricao': 'RADIOGRAFIA DE PE / DEDOS DO PE',
            },
            {
                'codigo': '0204060176',
                'descricao': 'RADIOGRAFIA PANORAMICA DE MEMBROS INFERIORES',
            },
        ],
    },
    '0903010046': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA EM ORTOPEDIA COM RECURSOS DE RADIOLOGIA E RESSONÂNCIA MAGNÉTICA',
        'itens_obrigatorios': [
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
            {
                'codigo': '0301010307',
                'descricao': 'TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0204020034',
                'descricao': 'RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO + OBLIQUAS)',
            },
            {
                'codigo': '0204020042',
                'descricao': 'RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO / FLEXAO)',
            },
            {
                'codigo': '0204020077',
                'descricao': 'RADIOGRAFIA DE COLUNA LOMBO-SACRA (C/ OBLIQUAS)',
            },
            {
                'codigo': '0204020085',
                'descricao': 'RADIOGRAFIA DE COLUNA LOMBO-SACRA FUNCIONAL / DINAMICA',
            },
            {
                'codigo': '0204020093',
                'descricao': 'RADIOGRAFIA DE COLUNA TORACICA (AP + LATERAL)',
            },
            {
                'codigo': '0204020107',
                'descricao': 'RADIOGRAFIA DE COLUNA TORACO-LOMBAR',
            },
            {
                'codigo': '0204020131',
                'descricao': 'RADIOGRAFIA PANORAMICA DE COLUNA TOTAL- TELESPONDILOGRAFIA ( P/ ESCOLIOSE)',
            },
            {
                'codigo': '0204040035',
                'descricao': 'RADIOGRAFIA DE ARTICULACAO ESCAPULO-UMERAL',
            },
            {'codigo': '0204040078', 'descricao': 'RADIOGRAFIA DE COTOVELO'},
            {'codigo': '0204040094', 'descricao': 'RADIOGRAFIA DE MAO'},
            {
                'codigo': '0204040116',
                'descricao': 'RADIOGRAFIA DE ESCAPULA/OMBRO (TRES POSICOES)',
            },
            {
                'codigo': '0204040124',
                'descricao': 'RADIOGRAFIA DE PUNHO (AP + LATERAL + OBLIQUA)',
            },
            {
                'codigo': '0204060060',
                'descricao': 'RADIOGRAFIA DE ARTICULACAO COXO-FEMORAL',
            },
            {'codigo': '0204060095', 'descricao': 'RADIOGRAFIA DE BACIA'},
            {'codigo': '0204060109', 'descricao': 'RADIOGRAFIA DE CALCANEO'},
            {
                'codigo': '0204060125',
                'descricao': 'RADIOGRAFIA DE JOELHO (AP + LATERAL)',
            },
            {
                'codigo': '0204060133',
                'descricao': 'RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + AXIAL)',
            },
            {
                'codigo': '0204060141',
                'descricao': 'RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + OBLIQUA + 3 AXIAIS)',
            },
            {
                'codigo': '0204060150',
                'descricao': 'RADIOGRAFIA DE PE / DEDOS DO PE',
            },
            {
                'codigo': '0204060176',
                'descricao': 'RADIOGRAFIA PANORAMICA DE MEMBROS INFERIORES',
            },
            {
                'codigo': '0207010030',
                'descricao': 'RESSONANCIA MAGNETICA DE COLUNA CERVICAL/PESCOÇO',
            },
            {
                'codigo': '0207010048',
                'descricao': 'RESSONANCIA MAGNETICA DE COLUNA LOMBO-SACRA',
            },
            {
                'codigo': '0207010056',
                'descricao': 'RESSONANCIA MAGNETICA DE COLUNA TORACICA',
            },
            {
                'codigo': '0207020027',
                'descricao': 'RESSONANCIA MAGNETICA DE MEMBRO SUPERIOR (UNILATERAL)',
            },
            {
                'codigo': '0207030022',
                'descricao': 'RESSONANCIA MAGNETICA DE BACIA / PELVE / ABDOMEN INFERIOR',
            },
            {
                'codigo': '0207030030',
                'descricao': 'RESSONANCIA MAGNETICA DE MEMBRO INFERIOR (UNILATERAL)',
            },
        ],
    },
    '0904010015': {
        'nome': 'OCI AVALIAÇÃO INICIAL DIAGNÓSTICA DE DÉFICIT AUDITIVO',
        'itens_obrigatorios': [
            {
                'codigo': '0211070041',
                'descricao': 'AUDIOMETRIA TONAL LIMIAR (VIA AEREA / OSSEA)',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0211070203', 'descricao': 'IMITANCIOMETRIA'}
        ],
    },
    '0904010023': {
        'nome': 'OCI PROGRESSÃO DA AVALIAÇÃO DIAGNÓSTICA DE DÉFICIT AUDITIVO',
        'itens_obrigatorios': [
            {
                'codigo': '0211070041',
                'descricao': 'AUDIOMETRIA TONAL LIMIAR (VIA AEREA / OSSEA)',
            },
            {
                'codigo': '0211070262',
                'descricao': 'POTENCIAL EVOCADO AUDITIVO DE CURTA MEDIA E LONGA LATENCIA',
            },
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0211050113',
                'descricao': 'POTENCIAL EVOCADO AUDITIVO',
            },
            {'codigo': '0211070203', 'descricao': 'IMITANCIOMETRIA'},
        ],
    },
    '0904010031': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA DE NASOFARINGE E DE OROFARINGE',
        'itens_obrigatorios': [
            {'codigo': '0209040025', 'descricao': 'LARINGOSCOPIA'},
            {'codigo': '0209040041', 'descricao': 'VIDEOLARINGOSCOPIA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [],
    },
    '0905010019': {
        'nome': 'OCI AVALIAÇÃO INICIAL EM OFTALMOGIA - 0 A 8 ANOS',
        'itens_obrigatorios': [
            {
                'codigo': '0211060020',
                'descricao': 'BIOMICROSCOPIA DE FUNDO DE OLHO',
            },
            {'codigo': '0211060127', 'descricao': 'MAPEAMENTO DE RETINA'},
            {'codigo': '0211060232', 'descricao': 'TESTE ORTÓPTICO'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [],
    },
    '0905010027': {
        'nome': 'OCI AVALIAÇÃO DE ESTRABISMO',
        'itens_obrigatorios': [
            {
                'codigo': '0211060020',
                'descricao': 'BIOMICROSCOPIA DE FUNDO DE OLHO',
            },
            {'codigo': '0211060127', 'descricao': 'MAPEAMENTO DE RETINA'},
            {'codigo': '0211060232', 'descricao': 'TESTE ORTÓPTICO'},
            {'codigo': '0211060259', 'descricao': 'TONOMETRIA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0211060100', 'descricao': 'FUNDOSCOPIA'},
            {
                'codigo': '0211060178',
                'descricao': 'RETINOGRAFIA COLORIDA BINOCULAR',
            },
        ],
    },
    '0905010035': {
        'nome': 'OCI AVALIAÇÃO INICIAL EM OFTALMOLOGIA - A PARTIR DE 9 ANOS',
        'itens_obrigatorios': [
            {
                'codigo': '0211060020',
                'descricao': 'BIOMICROSCOPIA DE FUNDO DE OLHO',
            },
            {'codigo': '0211060127', 'descricao': 'MAPEAMENTO DE RETINA'},
            {'codigo': '0211060259', 'descricao': 'TONOMETRIA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0211060232', 'descricao': 'TESTE ORTÓPTICO'}
        ],
    },
    '0905010043': {
        'nome': 'OCI AVALIAÇÃO DE RETINOPATIA DIABÉTICA',
        'itens_obrigatorios': [
            {
                'codigo': '0211060020',
                'descricao': 'BIOMICROSCOPIA DE FUNDO DE OLHO',
            },
            {'codigo': '0211060127', 'descricao': 'MAPEAMENTO DE RETINA'},
            {
                'codigo': '0211060178',
                'descricao': 'RETINOGRAFIA COLORIDA BINOCULAR',
            },
            {'codigo': '0211060259', 'descricao': 'TONOMETRIA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [],
    },
    '0905010051': {
        'nome': 'OCI AVALIAÇÃO INICIAL PARA ONCOLOGIA OFTALMOLÓGICA',
        'itens_obrigatorios': [
            {
                'codigo': '0205020089',
                'descricao': 'ULTRASSONOGRAFIA DE GLOBO OCULAR / ORBITA (MONOCULAR)',
            },
            {
                'codigo': '0211060020',
                'descricao': 'BIOMICROSCOPIA DE FUNDO DE OLHO',
            },
            {'codigo': '0211060127', 'descricao': 'MAPEAMENTO DE RETINA'},
            {'codigo': '0211060259', 'descricao': 'TONOMETRIA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {
                'codigo': '0211060178',
                'descricao': 'RETINOGRAFIA COLORIDA BINOCULAR',
            }
        ],
    },
    '0905010060': {
        'nome': 'OCI AVALIAÇÃO DIAGNÓSTICA EM NEURO OFTALMOLOGIA',
        'itens_obrigatorios': [
            {
                'codigo': '0211060020',
                'descricao': 'BIOMICROSCOPIA DE FUNDO DE OLHO',
            },
            {
                'codigo': '0211060038',
                'descricao': 'CAMPIMETRIA COMPUTADORIZADA OU MANUAL COM GRÁFICO',
            },
            {'codigo': '0211060127', 'descricao': 'MAPEAMENTO DE RETINA'},
            {
                'codigo': '0211060178',
                'descricao': 'RETINOGRAFIA COLORIDA BINOCULAR',
            },
            {'codigo': '0211060224', 'descricao': 'TESTE DE VISÃO DE CORES'},
            {'codigo': '0211060259', 'descricao': 'TONOMETRIA'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [],
    },
    '0905010078': {
        'nome': 'OCI EXAMES OFTALMOLÓGICOS SOB SEDAÇÃO',
        'itens_obrigatorios': [
            {'codigo': '0417010060', 'descricao': 'SEDACAO'},
            {
                'codigo': '0301010072',
                'descricao': 'CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA',
            },
        ],
        'itens_facultativos': [
            {'codigo': '0211060127', 'descricao': 'MAPEAMENTO DE RETINA'},
            {'codigo': '0211060259', 'descricao': 'TONOMETRIA'},
        ],
    },
}


def analisar_csv(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, delimiter=';', dtype=str)
    df = df[df['STATUS'] == '1']  # Filtrar apenas registros com STATUS == 1

    relatorio = []
    pacientes_em_agrupamentos = set()
    agrupamentos_encontrados = 0

    relatorio.append(
        "*********************    FORAM ENCONTRADOS {} CONJUNTOS DE OCI'S    ***********************\n"
    )

    for codigo, agrupamento in agrupamentos.items():
        codigos_obrigatorios = [
            item['codigo'] for item in agrupamento['itens_obrigatorios']
        ]
        codigos_facultativos = [
            item['codigo'] for item in agrupamento['itens_facultativos']
        ]

        pacientes_agrupados = []

        for paciente, dados_paciente in df.groupby('DOCUMENTO_PACIENTE'):
            codigos_paciente = set(dados_paciente['CODIGO_SIGTAP'])

            if all(c in codigos_paciente for c in codigos_obrigatorios):
                pacientes_agrupados.append(paciente)
                pacientes_em_agrupamentos.add(paciente)

        if pacientes_agrupados:
            agrupamentos_encontrados += 1
            relatorio.append(
                '_________________________________________________________________________________________'
            )
            relatorio.append(
                f"{codigo[:2]}.{codigo[2:4]}.{codigo[4:6]}.{codigo[6:]} - {agrupamento['nome']}\n"
            )

            for paciente in sorted(pacientes_agrupados):
                relatorio.append(f'--- {paciente}')
                for item in agrupamento['itens_obrigatorios']:
                    registros = df[
                        (df['DOCUMENTO_PACIENTE'] == paciente)
                        & (df['CODIGO_SIGTAP'] == item['codigo'])
                    ]
                    for _, registro in registros.iterrows():
                        relatorio.append(
                            f"-------- OBG\t{registro['CNES_SOLICITANTE']}\t{registro['DATA_SOLICITACAO']}\t{item['codigo']} - {item['descricao']}"
                        )
                for item in agrupamento['itens_facultativos']:
                    registros = df[
                        (df['DOCUMENTO_PACIENTE'] == paciente)
                        & (df['CODIGO_SIGTAP'] == item['codigo'])
                    ]
                    for _, registro in registros.iterrows():
                        relatorio.append(
                            f"-------- FAC\t{registro['CNES_SOLICITANTE']}\t{registro['DATA_SOLICITACAO']}\t{item['codigo']} - {item['descricao']}"
                        )

    # Atualiza cabeçalho com o número real de conjuntos encontrados
    relatorio[0] = relatorio[0].format(agrupamentos_encontrados)

    # Pacientes que não estão em nenhum agrupamento
    relatorio.append(
        '\n********************    PACIENTES QUE NÃO ESTÃO EM NENHUM CONJUNTO  ***********************'
    )
    pacientes_restantes = df[
        ~df['DOCUMENTO_PACIENTE'].isin(pacientes_em_agrupamentos)
    ]

    for _, linha in pacientes_restantes.iterrows():
        descricao = next(
            (
                item['descricao']
                for g in agrupamentos.values()
                for item in g['itens_obrigatorios'] + g['itens_facultativos']
                if item['codigo'] == linha['CODIGO_SIGTAP']
            ),
            'código não faz parte de uma item de OCI',
        )
        relatorio.append(
            f"--- {linha['CNES_SOLICITANTE']}\t{linha['DOCUMENTO_PACIENTE']}\t{linha['DATA_SOLICITACAO']}\t{linha['CODIGO_SIGTAP']} - {descricao}"
        )

    # Rodapé com data e hora
    relatorio.append('\n{:%d/%m/%Y %H:%M:%S}'.format(datetime.now()))
    return relatorio


def salvar_relatorio(relatorio, caminho_saida_csv, caminho_saida_pdf):
    # Salva como CSV
    with open(caminho_saida_csv, 'w', encoding='utf-8') as f:
        f.write('\n'.join(relatorio))

    # Salva como PDF em modo paisagem e fonte menor
    c = canvas.Canvas(caminho_saida_pdf, pagesize=landscape(letter))
    width, height = landscape(letter)

    c.setFont('Courier', 8)  # Fonte menor para caber mais texto
    y = height - 30
    margem_esquerda = 30

    for linha in relatorio:
        c.drawString(
            margem_esquerda, y, linha[:300]
        )  # Trunca só se for realmente muito grande
        y -= 10  # Espaço entre linhas menor
        if y < 30:
            c.showPage()
            c.setFont('Courier', 8)
            y = height - 30

    c.save()


def interface_grafica():
    def selecionar_arquivo():
        caminho_arquivo = filedialog.askopenfilename(
            filetypes=[('CSV files', '*.csv')]
        )
        if caminho_arquivo:
            relatorio = analisar_csv(caminho_arquivo)
            caminho_saida_csv = filedialog.asksaveasfilename(
                defaultextension='.csv', filetypes=[('CSV files', '*.csv')]
            )
            caminho_saida_pdf = filedialog.asksaveasfilename(
                defaultextension='.pdf', filetypes=[('PDF files', '*.pdf')]
            )
            if caminho_saida_csv and caminho_saida_pdf:
                salvar_relatorio(
                    relatorio, caminho_saida_csv, caminho_saida_pdf
                )
                messagebox.showinfo('Sucesso', 'Relatório gerado com sucesso!')

    root = tk.Tk()
    root.title('Analisador de CSV - OCI')
    root.geometry('320x100')

    btn_selecionar = tk.Button(
        root, text='Selecionar Arquivo CSV', command=selecionar_arquivo
    )
    btn_selecionar.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    interface_grafica()
"""
  "0903010038": {
        "nome": "OCI AVALIAÇÃO DIAGNÓSTICA EM ORTOPEDIA COM RECURSOS DE RADIOLOGIA E TOMOGRAFIA COMPUTADORIZADA",
        "itens_obrigatorios": [],
        "itens_facultativos": [
            {"codigo": "0204020034", "descricao": "RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO + OBLIQUAS)"},
            {"codigo": "0204020042", "descricao": "RADIOGRAFIA DE COLUNA CERVICAL (AP + LATERAL + TO / FLEXAO)"},
            {"codigo": "0204020077", "descricao": "RADIOGRAFIA DE COLUNA LOMBO-SACRA (C/ OBLIQUAS)"},
            {"codigo": "0204020085", "descricao": "RADIOGRAFIA DE COLUNA LOMBO-SACRA FUNCIONAL / DINAMICA"},
            {"codigo": "0204020093", "descricao": "RADIOGRAFIA DE COLUNA TORACICA (AP + LATERAL)"},
            {"codigo": "0204020107", "descricao": "RADIOGRAFIA DE COLUNA TORACO-LOMBAR"},
            {"codigo": "0204020131", "descricao": "RADIOGRAFIA PANORAMICA DE COLUNA TOTAL- TELESPONDILOGRAFIA ( P/ ESCOLIOSE)"},
            {"codigo": "0204040035", "descricao": "RADIOGRAFIA DE ARTICULACAO ESCAPULO-UMERAL"},
            {"codigo": "0204040078", "descricao": "RADIOGRAFIA DE COTOVELO"},
            {"codigo": "0204040094", "descricao": "RADIOGRAFIA DE MAO"},
            {"codigo": "0204040116", "descricao": "RADIOGRAFIA DE ESCAPULA/OMBRO (TRES POSICOES)"},
            {"codigo": "0204040124", "descricao": "RADIOGRAFIA DE PUNHO (AP + LATERAL + OBLIQUA)"},
            {"codigo": "0204060060", "descricao": "RADIOGRAFIA DE ARTICULACAO COXO-FEMORAL"},
            {"codigo": "0204060095", "descricao": "RADIOGRAFIA DE BACIA"},
            {"codigo": "0204060109", "descricao": "RADIOGRAFIA DE CALCANEO"},
            {"codigo": "0204060125", "descricao": "RADIOGRAFIA DE JOELHO (AP + LATERAL)"},
            {"codigo": "0204060133", "descricao": "RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + AXIAL)"},
            {"codigo": "0204060141", "descricao": "RADIOGRAFIA DE JOELHO OU PATELA (AP + LATERAL + OBLIQUA + 3 AXIAIS)"},
            {"codigo": "0204060150", "descricao": "RADIOGRAFIA DE PE / DEDOS DO PE"},
            {"codigo": "0204060176", "descricao": "RADIOGRAFIA PANORAMICA DE MEMBROS INFERIORES"},
            {"codigo": "0206010010", "descricao": "TOMOGRAFIA COMPUTADORIZADA DE COLUNA CERVICAL C/ OU S/ CONTRASTE"},
            {"codigo": "0206010028", "descricao": "TOMOGRAFIA COMPUTADORIZADA DE COLUNA LOMBO-SACRA C/ OU S/ CONTRASTE"},
            {"codigo": "0206010036", "descricao": "TOMOGRAFIA COMPUTADORIZADA DE COLUNA TORACICA C/ OU S/ CONTRASTE"},
            {"codigo": "0206020015", "descricao": "TOMOGRAFIA COMPUTADORIZADA DE ARTICULACOES DE MEMBRO SUPERIOR"},
            {"codigo": "0206020023", "descricao": "TOMOGRAFIA COMPUTADORIZADA DE SEGMENTOS APENDICULARES - (BRACO, ANTEBRAÇO, MÃO, COXA, PERNA, PÉ)"},
            {"codigo": "0206030029", "descricao": "TOMOGRAFIA COMPUTADORIZADA DE ARTICULACOES DE MEMBRO INFERIOR"},
            {"codigo": "0206030037", "descricao": "TOMOGRAFIA COMPUTADORIZADA DE PELVE / BACIA / ABDOMEN INFERIOR"},
            {"codigo": "0301010072", "descricao": "CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA"},
            {"codigo": "0301010307", "descricao": "TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA"}
        ]
    },
"""
