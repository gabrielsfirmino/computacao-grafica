from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from iluminacao import *
from objetos import *

angulo = 90
width, height = 600, 600
xe, ye, ze = 60, 30, 20
xlt, ylt, zlt = 0, 0, 0
xup, yup, zup = 0, 10, 0
	
def parametrosVisualizacao():
	aspecto = width / height

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(angulo,aspecto,0.5,500)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(xe, ye, ze, xlt, ylt, zlt, xup, yup, zup)

def inicializar():
	glClearColor(0,0,0,1)  
	iluminar()

def gerenciaTeclado(key, x, y):
	global xlt, ylt, zlt

	if (key == GLUT_KEY_LEFT):
		xlt = xlt+3
		zlt = zlt+20
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(xe, ye, ze, xlt, ylt, zlt, xup, yup, zup)

	if (key == GLUT_KEY_RIGHT):
		xlt = xlt-3
		zlt = zlt-20
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(xe, ye, ze, xlt, ylt, zlt, xup, yup, zup)

	if (key == GLUT_KEY_UP):
		ylt = ylt+10
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(xe, ye, ze, xlt, ylt, zlt, xup, yup, zup)
        
	if (key == GLUT_KEY_DOWN):
		ylt = ylt-10
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(xe, ye, ze, xlt, ylt, zlt, xup, yup, zup)

	glutPostRedisplay()

def gerenciaMouse(button, state, x, y):
	global xe, ye, ze
	
	if (button == GLUT_LEFT_BUTTON):
		xe = xe-3
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(xe, ye, ze, xlt, ylt, zlt, xup, yup, zup)

	if (button == GLUT_RIGHT_BUTTON):
		xe = xe+3
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(xe, ye, ze, xlt, ylt, zlt, xup, yup, zup)

	glutPostRedisplay()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(width, height)
	janela = glutCreateWindow("Janela") 
	glutReshapeFunc(parametrosVisualizacao())
	glutDisplayFunc(posicionarObjetos)
	glutMouseFunc(gerenciaMouse)
	glutSpecialFunc(gerenciaTeclado)
	inicializar()
	glutMainLoop()

main()