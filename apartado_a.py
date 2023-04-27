import pandas as pd
import numpy as np
from scipy.stats import norm

longitud=1
tiempo=0.46
error_longitud=0.01
error_tiempo=0.01

valores_longitud=np.random.normal(loc=longitud, scale=error_longitud, size=6000)
valores_tiempo=np.random.normal(loc=tiempo, scale= error_tiempo, size=6000)
valores_g=2*valores_longitud/valores_tiempo**2

tabla=pd.DataFrame({"Longitud": valores_longitud, "tiempo": valores_tiempo, "gravedad": valores_g})

print(tabla)

media=tabla.gravedad.mean()
desviacion_tipica=tabla.gravedad.std()

if media>=9.4 and media <10.4:
    probabilidad=norm.cdf(10.4, media, desviacion_tipica)- norm.cdf(9.4, media, desviacion_tipica)
    print("Estan en el planeta Tierra con una probabilidad de", probabilidad*100, "%")
elif  media <6.2:
    probabilidad=norm.cdf(6.2, media, desviacion_tipica)
    print("Estan en el planeta Marte con una probabilidad de", probabilidad*100, "%")
elif media>=17.9:
    probabilidad=1-norm.cdf(17.9, media, desviacion_tipica)
    print("Estan en el planeta Jupiter con una probabilidad de", probabilidad*100, "%")
elif media<9.4 and media >=8.85:
    probabilidad=norm.cdf(9.4, media, desviacion_tipica)- norm.cdf(8.85, media, desviacion_tipica)
    print("Estan en el planeta Saturno con una probabilidad de", probabilidad*100, "%")
elif media>=6.2 and media <8.85:
    probabilidad=norm.cdf(8.85, media, desviacion_tipica)- norm.cdf(6.2, media, desviacion_tipica)
    print("Estan en el planeta tierra con una probabilidad de", probabilidad*100, "%")
elif media>=10.4 and media <17.9:
    probabilidad=norm.cdf(17.9, media, desviacion_tipica)- norm.cdf(10.4, media, desviacion_tipica)
    print("Estan en el planeta tierra con una probabilidad de", probabilidad*100, "%")
