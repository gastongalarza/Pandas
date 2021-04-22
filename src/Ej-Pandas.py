#PANDAS

import pandas as pd
from google.colab import files
import io
from statistics import mode
from collections import Counter
import datetime

print("Subir el archivo orders_dataset.csv\n")
uploaded = files.upload()
df_orders = pd.read_csv(io.BytesIO(uploaded['orders_dataset.csv']))

print("Subir el archivo product_names.csv\n")
uploaded = files.upload()
df_product_names = pd.read_csv(io.BytesIO(uploaded['product_names.csv']))


productos = df_orders['PRODUCT_ID']
fechas = df_orders['ORDER_DATE']
ordenes = df_orders['ORDER_ID']


def producto_mas_vendido(lista_productos):
  return Counter(lista_productos).most_common()[0][0] 

def get_productos_del_mes(mes):
  return productos[df_orders['ORDER_DATE'].dt.month == mes]

def nombre_producto_mas_vendido_mes(mes):
  return nombre_producto_mas_vendido(get_productos_del_mes(mes))

def cantidad_productos_orden(order_id):
 return len(df_orders[df_orders.ORDER_ID==order_id].PRODUCT_ID)

def get_producto_segun_nombre(nombre_producto):
  return df_product_names[df_product_names.NAME == nombre_producto].PRODUCT_ID


#Punto_1
def nombre_producto_mas_vendido(lista_productos):
  print(df_product_names[df_product_names.PRODUCT_ID == producto_mas_vendido(lista_productos)].NAME)


#Punto_2
def nombre_producto_mas_vendido_cada_mes():
  for mes in set(fechas.dt.month):
    print("En el mes",+mes, "el producto mas vendido fue:\n ")
    print(nombre_producto_mas_vendido_mes(mes))
    print("\n")

#Punto_3
def cantidad_de_productos_promedio_por_orden():
  for orden in set(lista_ordenes):
    print("El promedio de la orden",+orden,"es: \n ", cantidad_productos_orden(orden))

#Punto_4 (Opcional)
# Calcular en que fechas se ha vendido un producto determinado
def fecha_producto_vendido(nombre_producto): 
   print(df_orders[df_orders.PRODUCT_ID == get_producto_segun_nombre(nombre_producto)].ORDER_DATE)