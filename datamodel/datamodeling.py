import pymysql as py
import pandas as pd
import matplotlib.pyplot as plt
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

class DataBase:
    def __init__(self):
        self.connection=py.connect(
            host='127.0.0.1',
            user='root',
            password='',
            db='bd de psicología'
        )
        self.cursor=self.connection.cursor()

    print('Conexión establecida')

    def select_user(self):
        sql='SELECT * FROM preguntas;'
        try:
            self.cursor.execute(sql)
            user=self.cursor.fetchall()
            for u in user:
                print("P1: ",user[0])
                print("P2: ", user[1])
                print("P3: ", user[2])
                print("P3: ", user[3])
                print("------------------------------")
        except Exception as e:
            raise

    def update(self):
        print("Ingrese el número de la pregunta para la respuesta a modificar (1-5)")
        id_pregunta=int(input())
        id_pregunta=id_pregunta+99
        sql=''
        if id_pregunta==100:
            print("Ingrese el id de la respuesta para modificar su cantidad (100-103)")
            idr=int(input())
            print("Ingrese la cantidad a insertar")
            cant = int(input())
            sql = f'Update respuestas set cantidad_respondida={cant} where id_respuesta={idr};'
        else:
            if id_pregunta==101:
                print("Ingrese el id de la respuesta para modificar su cantidad (104-110)")
                idr = int(input())
                print("Ingrese la cantidad a insertar")
                cant = int(input())
                sql = f'Update respuestas set cantidad_respondida={cant} where id_respuesta={idr};'
            else:
                if id_pregunta==102:
                    print("Ingrese el id de la respuesta para modificar su cantidad (111-116)")
                    idr = int(input())
                    print("Ingrese la cantidad a insertar")
                    cant = int(input())
                    sql = f'Update respuestas set cantidad_respondida={cant} where id_respuesta={idr};'
                else:
                    if id_pregunta==103:
                        print("Ingrese el id de la respuesta para modificar su cantidad (117-123)")
                        idr = int(input())
                        print("Ingrese la cantidad a insertar")
                        cant = int(input())
                        sql = f'Update respuestas set cantidad_respondida={cant} where id_respuesta={idr};'
                    else:
                        if id_pregunta==104:
                            print("Ingrese el id de la respuesta para modificar su cantidad (124-132)")
                            idr = int(input())
                            print("Ingrese la cantidad a insertar")
                            cant = int(input())
                            sql = f'Update respuestas set cantidad_respondida={cant} where id_respuesta={idr};'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise


class Preguntas:

    def pregunta1(self):
        database = DataBase()
        database.update()
        sql = 'SELECT * FROM respuestas where id_pregunta=100;'
        sql2 = 'SELECT *FROM preguntas where id_pregunta=100;'
        data = pd.read_sql(sql, database.connection)
        data2 = pd.read_sql(sql2, database.connection)
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(data2)
        d1 = df['Cantidad_respondida'].values
        d2 = df['Respuesta'].values
        d3 = df2['Pregunta'].values

        fig = plt.figure(figsize=(8.5, 5))
        fig.tight_layout()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(d2, d1, edgecolor='black', color='cyan')
        plt.title(d3[0])
        plt.savefig(f'.\datamodel\Graficos\GraficoP1.png')

    def pregunta2(self):
        database = DataBase()
        database.update()
        sql = 'SELECT * FROM respuestas where id_pregunta=101;'
        sql2 = 'SELECT *FROM preguntas where id_pregunta=101;'
        data = pd.read_sql(sql, database.connection)
        data2 = pd.read_sql(sql2, database.connection)
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(data2)
        d1 = df['Cantidad_respondida'].values
        d2 = df['Respuesta'].values
        d3 = df2['Pregunta'].values

        fig = plt.figure(figsize=(10, 5))
        fig.tight_layout()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(d2, d1, edgecolor='black', color='orange')
        plt.title(d3[0])
        plt.savefig(f'.\datamodel\Graficos\GraficoP2.png')

    def pregunta3(self):
        database = DataBase()
        database.update()
        sql = 'SELECT * FROM respuestas where id_pregunta=102;'
        sql2 = 'SELECT *FROM preguntas where id_pregunta=102;'
        data = pd.read_sql(sql, database.connection)
        data2 = pd.read_sql(sql2, database.connection)
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(data2)
        d1 = df['Cantidad_respondida'].values
        d2 = df['Respuesta'].values
        d3 = df2['Pregunta'].values

        fig = plt.figure(figsize=(10, 5))
        fig.tight_layout()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(d2, d1, edgecolor='black', color='red')
        plt.title(d3[0])
        plt.savefig(f'.\datamodel\Graficos\GraficoP3.png')

    def pregunta4(self):
        database = DataBase()
        database.update()
        sql = 'SELECT * FROM respuestas where id_pregunta=103;'
        sql2 = 'SELECT *FROM preguntas where id_pregunta=103;'
        data = pd.read_sql(sql, database.connection)
        data2 = pd.read_sql(sql2, database.connection)
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(data2)
        d1 = df['Cantidad_respondida'].values
        d2 = df['Respuesta'].values
        d3 = df2['Pregunta'].values

        fig = plt.figure(figsize=(16, 5))
        fig.tight_layout()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(d2, d1, edgecolor='black', color='blue')
        plt.title(d3[0])
        plt.savefig(f'.\datamodel\Graficos\GraficoP4.png')

    def pregunta5(self):
        database = DataBase()
        database.update()
        sql = 'SELECT * FROM respuestas where id_pregunta=104;'
        sql2 = 'SELECT *FROM preguntas where id_pregunta=104;'
        data = pd.read_sql(sql, database.connection)
        data2 = pd.read_sql(sql2, database.connection)
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(data2)
        d1 = df['Cantidad_respondida'].values
        d2 = df['Respuesta'].values
        d3 = df2['Pregunta'].values
        fig = plt.figure(figsize=(16, 5))
        fig.tight_layout()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(d2, d1, edgecolor='black', color='purple')
        plt.title(d3[0])
        plt.savefig(f'.\datamodel\Graficos\GraficoP5.png')


def enviar_correo():
    database = DataBase()
    print("Ingrese el id del profesor encargado")
    id_profesor=int(input())
    sql = f'SELECT * FROM profesores_encargados where id_profesor={id_profesor};'
    sql3 = 'SELECT *FROM preguntas'
    data = pd.read_sql(sql, database.connection)
    data3 = pd.read_sql(sql3, database.connection)
    df = pd.DataFrame(data)
    df3 = pd.DataFrame(data3)
    nom_dest = df['Nom_Profesor'].values
    nom_desti = nom_dest[0]
    user = 'relis.mybot@gmail.com'
    password = 'RelisIntech'
    desti = df['Correo_Profesor'].values
    destinatario=desti[0]
    print(destinatario)
    asunto = 'Correo de prueba'
    message = MIMEMultipart("alternative")
    message["Subject"] = asunto
    message["From"] = user
    message["To"] = destinatario
    html = f"""
    <html>
        <body>
            <p>
                Hola {nom_desti},<br>
                Espero que te encuentres bien, en este correo encontrará los gráficos de la 
                cantidad de respuestas a las preguntas
                hechas por los alumnos de la carrera a la que está asignado.<br>
                El <b>GraficoP1</b> es sobre el tema de nivel de estrés de los participantes, 
                el <b>GraficoP2</b> es sobre los factores que los participantes creen que hayan
                influido en el desarrollo de su estrés, el <b>GraficoP3</b> trata 
                de los principales cambios que han notado los participantes en sí mismos, el
                <b>GraficoP4</b> aborda los factores negativos que influyen en el estado de ánimo
                de los participantes, y finalmente el <b>GraficoP5</b> podrá ver los principales 
                efectos físicos que han notado los participantes.
            </p>
        </body>
    </html>
    """

    parte_html = MIMEText(html, "html")
    message.attach(parte_html)
    imagen1 = ".\datamodel\Graficos\GraficoP1.png"
    imagen2 = ".\datamodel\Graficos\GraficoP2.png"
    imagen3 = ".\datamodel\Graficos\GraficoP3.png"
    imagen4 = ".\datamodel\Graficos\GraficoP4.png"
    imagen5 = ".\datamodel\Graficos\GraficoP5.png"

    with open(imagen1, "rb") as adjunto:
        contenido_adjunto = MIMEBase("application", "octet-stream")
        contenido_adjunto.set_payload(adjunto.read())
    with open(imagen2, "rb") as adjunto:
        contenido_adjunto2 = MIMEBase("application", "octet-stream")
        contenido_adjunto2.set_payload(adjunto.read())
    with open(imagen3, "rb") as adjunto:
        contenido_adjunto3 = MIMEBase("application", "octet-stream")
        contenido_adjunto3.set_payload(adjunto.read())
    with open(imagen4, "rb") as adjunto:
        contenido_adjunto4 = MIMEBase("application", "octet-stream")
        contenido_adjunto4.set_payload(adjunto.read())
    with open(imagen5, "rb") as adjunto:
        contenido_adjunto5 = MIMEBase("application", "octet-stream")
        contenido_adjunto5.set_payload(adjunto.read())

    encoders.encode_base64(contenido_adjunto)
    encoders.encode_base64(contenido_adjunto2)
    encoders.encode_base64(contenido_adjunto3)
    encoders.encode_base64(contenido_adjunto4)
    encoders.encode_base64(contenido_adjunto5)

    contenido_adjunto.add_header(f"Content-Disposition", f"attachment; filename=GraficoP1.png")
    contenido_adjunto2.add_header(f"Content-Disposition", f"attachment; filename=GraficoP2.png")
    contenido_adjunto3.add_header(f"Content-Disposition", f"attachment; filename=GraficoP3.png")
    contenido_adjunto4.add_header(f"Content-Disposition", f"attachment; filename=GraficoP4.png")
    contenido_adjunto5.add_header(f"Content-Disposition", f"attachment; filename=GraficoP5.png")

    message.attach(contenido_adjunto)
    message.attach(contenido_adjunto2)
    message.attach(contenido_adjunto3)
    message.attach(contenido_adjunto4)
    message.attach(contenido_adjunto5)

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user, password)
        server.sendmail(user, destinatario, text)
        print("Mensaje enviado")

database=DataBase()

pregunta=Preguntas()
print("¿Qué gráfico desea mostrar, y data a modificar(1-5), ingrese otro número para pasar directamente a la parte del correo?")
respuesta=int(input())

if respuesta==1:
    pregunta.pregunta1()
else:
    if respuesta==2:
        pregunta.pregunta2()
    else:
        if respuesta==3:
            pregunta.pregunta3()
        else:
            if respuesta==4:
                pregunta.pregunta4()
            else:
                if respuesta==5:
                    pregunta.pregunta5()

plt.show()

print("¿Desea enviar un reporte al profesor encargado? (si/no)")
resp=input()
if resp=="si":
    enviar_correo()
else:
    if resp=="no":
        print("Fin del programa")


