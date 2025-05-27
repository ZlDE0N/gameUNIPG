import pyassimp
from OpenGL.GL import *

class Model:
    def __init__(self, meshes):
        self.meshes = meshes

def load_model(path):
    with pyassimp.load(path, processing=pyassimp.postprocess.aiProcess_Triangulate) as scene:
        print(f"Model loaded: {len(scene.meshes)} meshes")
        meshes_copy = []
        for mesh in scene.meshes:
            mesh_copy = type('Mesh', (), {})()
            mesh_copy.faces = list(mesh.faces)
            mesh_copy.vertices = list(mesh.vertices)
            mesh_copy.normals = list(mesh.normals) if hasattr(mesh, 'normals') else None
            meshes_copy.append(mesh_copy)
        return Model(meshes_copy)

def draw_model(model):
    if not model or not hasattr(model, "meshes"):
        print("❌ No model or meshes to draw.")
        return

    for mesh in model.meshes:
        print(f"✅ Drawing mesh with {len(mesh.vertices)} vertices")
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for idx in face:
                if mesh.normals:
                    glNormal3f(*mesh.normals[idx])
                glVertex3f(*mesh.vertices[idx])
        glEnd()
