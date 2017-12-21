from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angulo = 90

def iluminar():
	luzAmbiente = [0.2,0.2,0.2,1.0] 
	luzDifusa = [0.7,0.7,0.7,1.0]
	luzEspecular = [1.0, 1.0, 1.0, 1.0]
	posicaoLuz = [-30.0, 5.0, 20.0, 1.0]
	especularidade = [1.0,1.0,1.0,1.0]
	especMaterial = 60
	
	glShadeModel(GL_SMOOTH)

	glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
	glMateriali(GL_FRONT,GL_SHININESS,especMaterial)
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

	glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
	glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
	glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

	glEnable(GL_COLOR_MATERIAL)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)