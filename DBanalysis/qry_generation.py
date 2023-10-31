# # import test3
# class qrySwitch:
#   total_seats = " SUM(\"Seats\") "
#   total_pax = " SUM(\"Total pax\") "
#   total_rev = " SUM(\"Rev\") "

# class airports:
#   from_india = "FROM cirium_traffic_asia WHERE \"Orig\" IN ('IXA', 'AMD', 'ATQ', 'BLR', 'BBI', 'MAA', 'CJB', 'DED', 'DEL', 'JWR', 'GOI', 'GOX', 'GAY', 'GAU', 'HYD', 'IMF', 'IDR', 'JAI', 'CNN', 'COK', 'CCU', 'CCJ', 'LKO', 'IXM', 'IXE', 'BOM', 'NAG',  'PNQ', 'IXR', 'IXB', 'SXR', 'STV', 'TRV', 'TIR', 'TRZ', 'BDQ', 'VNS', 'VGA', 'VTZ')"
#   from_usa = ""

# def monthGenerator(year, num):
#     month = ''
#     month2 = ''
#     if (num > 12 & num < 1):
#             return 0
#     if (num >= 10 & num <= 12):
#             month = '-' + str(num) + "-01 00:00:00' "
#             month2 = '-' + str(num) + "-02 00:00:00'"
#     else:
#       month = '-0' + str(num) + "-01 00:00:00' "
#       month2 = '-0' + str(num) + "-02 00:00:00'"
#     return "BETWEEN " + "'" + str(year) + month + 'AND ' + str(year) + month2

# def biannualGenerator(year, num):
#     if (num >= 3 & num <= 0):
#       return 'error'
#     if (num == 1):
#       return "BETWEEN " + "'" + str(year) + "-01-01 00:00:00' " + 'AND ' + str(year) + "-06-02 00:00:00' "
#     else:
#       return "BETWEEN " + "'" + str(year) + "-07-01 00:00:00' " + 'AND ' + str(year) + "-12-02 00:00:00' "

# def qryGenerator(qry, interval, year, num):
#     intv = ''
#     if (interval == 'month'):
#       intv = monthGenerator(year, num)
#     elif (interval == 'biannual'):
#       intv = biannualGenerator(year, num)

#     if (qry == 'total_seats'):
#       qry = qrySwitch.total_seats
#     elif (qry == 'total_pax'):
#       qry = qrySwitch.total_pax
#     return 'SELECT ' + qry + "AND \"Year-Month-Day\" " + intv

# print(qryGenerator('total_seats', 'month','2022', 11))

locationDict = {"fromUs" : """WHERE "Orig" IN 
             ('ABE', 'ABI', 'ABR', 'ABY', 'ACK', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 'AGS', 
             'AKC', 'ALB', 'ALW', 'AMA', 'ANC', 'APN', 'ASE', 'ATL', 'ATW', 'AUG', 'AUS', 'AVL', 
             'AVP', 'AZO', 'BDL', 'BET', 'BFF', 'BFL', 'BGM', 'BGR', 'BHM', 'BIL', 'BIS', 'BLI', 
             'BMI', 'BNA', 'BOI', 'BOS', 'BPT', 'BQK', 'BQN', 'BRO', 'BRW', 'BTM', 'BTR', 'BTV', 
             'BUF', 'BUR', 'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CEC', 'CHA', 'CHO', 'CHS', 'CIC', 
             'CID', 'CKB', 'CLD', 'CLE', 'CLL', 'CLT', 'CMH', 'CMI', 'COD', 'COS', 'CPR', 'CRP', 'CRW', 
             'CSG', 'CVG', 'CWA', 'DAB', 'DAL', 'DAY', 'DBQ', 'DCA', 'DEN', 'DFW', 'DHN', 'DIK', 'DLG',
              'DLH', 'DRO', 'DSM', 'DTW', 'DVL', 'EAR', 'EAT', 'EAU', 'ECP', 'EGE', 'EKO', 'ELM', 'ELP', 
             'ERI', 'EUG', 'EVV', 'EWN', 'EWR', 'EYW', 'FAI', 'FAR', 'FAT', 'FAY', 'FCA', 'FCM', 'FLL', 
             'FLO', 'FNT', 'FSD', 'FSM', 'FWA', 'FYV', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV', 'GPT', 'GRB', 
             'GRI', 'GRK', 'GRR', 'GSO', 'GSP', 'GST', 'GTF', 'GTR', 'GUC', 'HNL', 'HOB', 'HOU', 'HPN', 
             'HRL', 'HSV', 'HTS', 'IAD', 'IAH', 'ICT', 'IDA', 'ILG', 'IND', 'INL', 'ISN', 'ISP', 'ITH', 'ITO', 
             'IYK', 'JAC', 'JAN', 'JAX', 'JFK', 'JNU', 'KTN', 'LAN', 'LAS', 'LAX', 'LBB', 'LBE', 'LBF', 'LCH', 
             'LCK', 'LEW', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LMT', 'LNK', 'LRD', 'LSE', 'LWB', 'LYH',
              'MBS', 'MCI', 'MCN', 'MCO', 'MDT', 'MDW', 'MEI', 'MEM', 'MFE', 'MFR', 'MHT', 'MIA', 'MKE', 'MKG', 
             'MLB', 'MLU', 'MOB', 'MOD', 'MOT', 'MQT', 'MVY', 'MYR', 'OAJ', 'OAK', 'OGG', 'OKC', 'OMA', 'ONT', 
             'ORD', 'ORF', 'OTZ', 'OXR', 'PBI', 'PDX', 'PGD', 'PHL', 'PHX', 'PIE', 'PIR', 'PIT', 'PSC', 'PSG', 'PSP', 
             'PVD', 'PWM', 'RAP', 'RDD', 'RDM', 'RDU', 'RFD', 'RHI', 'RIC', 'RNO', 'ROC', 'ROW', 'RST', 'RSW', 'SAF', 
             'SAN', 'SAT', 'SAV', 'SBA', 'SCE', 'SDF', 'SEA', 'SFB', 'SFO', 'SJC', 'SJT', 'SJU', 'SLC', 'SMF', 'SNA', 
             'SPI', 'SPN', 'SRQ', 'STC', 'STL', 'STT', 'STX', 'SUN', 'SWF', 'SYR', 'TLH', 'TOL', 'TPA', 'TRI', 'TTN', 
             'TUL', 'TUS', 'TVC', 'TWF', 'TXK', 'TYR', 'TYS', 'UIN', 'USA', 'VLD', 'VPS', 'WRG', 'WYS', 'XNA', 'YAK', 'YUM')
"""}

selectDict = {"pax" : "SUM(\"Total Pax\")"}

def traLocGenerator(iata):
    return 

print(selectDict["pax"] + ' ' +locationDict["fromUs"])