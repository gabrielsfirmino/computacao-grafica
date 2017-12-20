import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 600, 600

def adicionarVertice(x, y, z):
    v = [x, y, z]
    return v

def adicionarFace(x, y, z):
    f = [x, y, z]
    return f

def importarObj(arquivo):
    vertices = []
    faces = []

    with open(arquivo) as file:
        i = 1
        for line in file:

            if line.startswith('#'): continue

            values = line.split()

            if not values: continue

            if values[0] == 'v':
                vertices.append(adicionarVertice(float(values[1]), float(values[2]), float(values[3])))
            
            if values[0] == 'f':
                faces.append(adicionarFace(float(values[1]), float(values[2]), float(values[3])))

    return vertices, faces
	
def parametrosVisualizacao():
	aspecto = width / height

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(90,aspecto,0.5,500)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(60,30,20, 0,0,0, 0.0,10.0,0.0)

def desenharObjeto(objeto):
	for countf in xrange(0, len(objeto[1])):
		vx, vy, vz = int(objeto[1][countf][0]), int(objeto[1][countf][1]), int(objeto[1][countf][2])

		glBegin(GL_POLYGON)
		glVertex3f(objeto[0][vx-1][0], objeto[0][vx-1][1], objeto[0][vx-1][2]) 
		glVertex3f(objeto[0][vy-1][0], objeto[0][vy-1][1], objeto[0][vy-1][2]) 
		glVertex3f(objeto[0][vz-1][0], objeto[0][vz-1][1], objeto[0][vz-1][2]) 
		glEnd()

def posicionarObjetos():	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMatrixMode(GL_MODELVIEW)
	glFlush()

	plano2 = importarObj("Objetos/plano2.obj")
	glPushMatrix() 
	glColor3f(0.2, 0.14, 0.89)
	desenharObjeto(plano2)
	glPopMatrix()

	parede3 = importarObj("Objetos/parede3.obj")
	glPushMatrix() 
	glTranslatef(0, 0, -80)
	glColor3f(0.5, 0.5, 0.5)
	desenharObjeto(parede3)
	glPopMatrix()

	parede2 = importarObj("Objetos/parede2.obj")
	glPushMatrix() 
	glColor3f(0.5, 0.5, 0.5)
	desenharObjeto(parede2)
	glPopMatrix()

	parede1 = importarObj("Objetos/parede1.obj")
	glPushMatrix() 
	glColor3f(0.5, 0.5, 0.5)
	desenharObjeto(parede1)
	glPopMatrix()

	cama = importarObj("Objetos/cama.obj")
	glPushMatrix() 
	glColor3f(0.59, 0.39, 0.0)
	desenharObjeto(cama)
	glPopMatrix()

	cochao = importarObj("Objetos/cochao.obj")
	glPushMatrix() 
	glColor3f(0.5, 1.0, 0.0)
	desenharObjeto(cochao)
	glPopMatrix()

	tv = importarObj("Objetos/tv.obj")
	glPushMatrix() 
	glColor3f(0.5, 0.0, 0.0)
	desenharObjeto(tv)
	glPopMatrix()

	cadeira = importarObj("Objetos/cadeira.obj")
	glPushMatrix() 
	glColor3f(0.59, 0.29, 0.0)
	desenharObjeto(cadeira)
	glPopMatrix()

	sofa = importarObj("Objetos/sofa.obj")
	glPushMatrix() 
	glColor3f(0.67, 0.08, 0.24)
	desenharObjeto(sofa)
	glPopMatrix()

	almofadas = importarObj("Objetos/almofadas.obj")
	glPushMatrix() 
	glColor3f(0.86, 0.78, 0.47)
	desenharObjeto(almofadas)
	glPopMatrix()

	mesa2 = importarObj("Objetos/mesa2.obj")
	glPushMatrix() 
	glColor3f(0.59, 0.29, 0.0)
	desenharObjeto(mesa2)
	glPopMatrix()

	lamp = importarObj("Objetos/lamp.obj")
	glPushMatrix() 
	glColor3f(0.31, 0.78, 0.47)
	desenharObjeto(lamp)
	glPopMatrix()

	supp = importarObj("Objetos/supp.obj")
	glPushMatrix() 
	glColor3f(0.47, 0.53, 0.6)
	desenharObjeto(supp)
	glPopMatrix()

	glColor3f(1, 1, 1);

	    # // Draw Body
	glPushMatrix()
	glTranslatef(0.0 ,0.75, 0.0);
	glutSolidSphere(0.75,20,20);

	    # // Draw Head
	glTranslatef(0.0, 1.0, 0.0);
	glutSolidSphere(0.25,20,20);

	    # // Draw Eyes
	glPushMatrix();
	glColor3f(0.0,0.0,0.0);
	glTranslatef(0.05, 0.10, 0.18);
	glutSolidSphere(0.05,10,10);
	glTranslatef(-0.1, 0.0, 0.0);
	glutSolidSphere(0.05,10,10);
	glPopMatrix();

	    # // Draw Nose
	glColor3f(1.0, 0.5 , 0.5);
	glRotatef(0.0,1.0, 0.0, 0.0);
	glutSolidCone(0.08,0.5,10,2);

	glutSwapBuffers() 

def inicializar():
	glClearColor(0,0,0,1)  

	# luzAmbiente = [0.2,0.2,0.2,1.0] 
	# luzDifusa = [0.7,0.7,0.7,1.0]
	# luzEspecular = [1.0, 1.0, 1.0, 1.0]
	# posicaoLuz = [-30.0, 5.0, 20.0, 1.0]

	# # // Capacidade de brilho do material
	# especularidade = [1.0,1.0,1.0,1.0]
	# especMaterial = 60
	
	# # // Habilita o modelo de colorizacao de Gouraud
	# glShadeModel(GL_SMOOTH)

	# # // Define a refletancia do material 
	# glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
	# # // Define a concentracao do brilho
	# glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

	# # // Ativa o uso da luz ambiente 
	# glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

	# # // Define os parametros da luz de numero 0
	# glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
	# glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
	# glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
	# glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

	# # // Habilita a definicao da cor do material a partir da cor corrente
	# glEnable(GL_COLOR_MATERIAL)
	# # //Habilita o uso de iluminacao
	# glEnable(GL_LIGHTING)
	# # // Habilita a luz de numero 0
	# glEnable(GL_LIGHT0)
	# # // Habilita o depth-buffering
	# glEnable(GL_DEPTH_TEST)

	# angle = 90

	# LuzAmbiente = [0.2,0.2,0.2,1.0] 
	# LuzDifusa = [0.7,0.7,0.7,1.0]
	# LuzEspecular = [1.0, 1.0, 1.0, 1.0]
	# PosicaoLuz0 = [-30.0, 5.0, 20.0, 1.0]
	# PosicaoLuz1 = [30.0, -5.0, -20.0, 1.0]
	# Especularidade = [1.0, 1.0, 1.0, 1.0]

	# glEnable(GL_COLOR_MATERIAL)

	# glEnable(GL_LIGHTING)

	# glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LuzAmbiente)
	# glLightfv(GL_LIGHT0, GL_AMBIENT, LuzAmbiente)
	# glLightfv(GL_LIGHT0, GL_DIFFUSE, LuzDifusa  )
	# glLightfv(GL_LIGHT0, GL_SPECULAR, LuzEspecular  )
	# glLightfv(GL_LIGHT0, GL_POSITION, PosicaoLuz0 )
	# glEnable(GL_LIGHT0)
	      
	# glEnable(GL_COLOR_MATERIAL)
	      
	# glMaterialfv(GL_FRONT,GL_SPECULAR, Especularidade)
	      
	# glMateriali(GL_FRONT,GL_SHININESS,51)
	      
	# glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LuzAmbiente)
	      
	# glLightfv(GL_LIGHT1, GL_AMBIENT, LuzAmbiente)
	# glLightfv(GL_LIGHT1, GL_DIFFUSE, LuzDifusa  )
	# glLightfv(GL_LIGHT1, GL_SPECULAR, LuzEspecular  )
	# glLightfv(GL_LIGHT1, GL_POSITION, PosicaoLuz1 )
	# glEnable(GL_LIGHT1)
	      
	# glEnable(GL_COLOR_MATERIAL)
	     
	# glMaterialfv(GL_FRONT,GL_SPECULAR, Especularidade)
	     
	# glMateriali(GL_FRONT,GL_SHININESS,20)

# def teclado(tecla, x, y):


def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(width, height)
	janela = glutCreateWindow("Janela") 
	glutReshapeFunc(parametrosVisualizacao())
	glutDisplayFunc(posicionarObjetos)
	# glutKeyboardFunc(teclado)
	inicializar()
	glutMainLoop()

main()