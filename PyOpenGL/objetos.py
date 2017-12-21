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

def importarObjeto(arquivo):
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

    plano2 = importarObjeto("Objetos/plano2.obj")
    glPushMatrix() 
    glColor3f(0.2, 0.14, 0.89)
    desenharObjeto(plano2)
    glPopMatrix()

    parede3 = importarObjeto("Objetos/parede3.obj")
    glPushMatrix() 
    glTranslatef(0, 0, -80)
    glColor3f(0.5, 0.5, 0.5)
    desenharObjeto(parede3)
    glPopMatrix()

    parede2 = importarObjeto("Objetos/parede2.obj")
    glPushMatrix() 
    glColor3f(0.5, 0.5, 0.5)
    desenharObjeto(parede2)
    glPopMatrix()

    parede1 = importarObjeto("Objetos/parede1.obj")
    glPushMatrix() 
    glColor3f(0.5, 0.5, 0.5)
    desenharObjeto(parede1)
    glPopMatrix()

    cama = importarObjeto("Objetos/cama.obj")
    glPushMatrix() 
    glColor3f(0.59, 0.39, 0.0)
    desenharObjeto(cama)
    glPopMatrix()

    cochao = importarObjeto("Objetos/cochao.obj")
    glPushMatrix() 
    glColor3f(0.5, 1.0, 0.0)
    desenharObjeto(cochao)
    glPopMatrix()

    tv = importarObjeto("Objetos/tv.obj")
    glPushMatrix() 
    glColor3f(0.5, 0.0, 0.0)
    desenharObjeto(tv)
    glPopMatrix()

    cadeira = importarObjeto("Objetos/cadeira.obj")
    glPushMatrix() 
    glColor3f(0.59, 0.29, 0.0)
    desenharObjeto(cadeira)
    glPopMatrix()

    sofa = importarObjeto("Objetos/sofa.obj")
    glPushMatrix() 
    glColor3f(0.67, 0.08, 0.24)
    desenharObjeto(sofa)
    glPopMatrix()

    almofadas = importarObjeto("Objetos/almofadas.obj")
    glPushMatrix() 
    glColor3f(0.86, 0.78, 0.47)
    desenharObjeto(almofadas)
    glPopMatrix()

    mesa2 = importarObjeto("Objetos/mesa2.obj")
    glPushMatrix() 
    glColor3f(0.59, 0.29, 0.0)
    desenharObjeto(mesa2)
    glPopMatrix()

    lamp = importarObjeto("Objetos/lamp.obj")
    glPushMatrix() 
    glColor3f(0.31, 0.78, 0.47)
    desenharObjeto(lamp)
    glPopMatrix()

    supp = importarObjeto("Objetos/supp.obj")
    glPushMatrix() 
    glColor3f(0.47, 0.53, 0.6)
    desenharObjeto(supp)
    glPopMatrix()

    glutSwapBuffers() 