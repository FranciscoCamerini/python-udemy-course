from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
format = dt.strftime('%A, %d de %B de %Y')
print(format)
print(mdays[mes_atual])