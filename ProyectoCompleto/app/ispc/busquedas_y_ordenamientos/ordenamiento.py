import pickle
import os

class OrdenamientoUsuarios:
    ARCHIVO_ORDENADO = 'data/usuariosOrdenadosPorUsername.ispc'
    
    @staticmethod
    def ordenar_por_username(usuarios):
        # Crear una copia para no modificar la lista original
        usuarios_ordenados = usuarios.copy()
        
        n = len(usuarios_ordenados)
        for i in range(n):
            for j in range(0, n-i-1):
                if usuarios_ordenados[j].get_username() > usuarios_ordenados[j+1].get_username():
                    usuarios_ordenados[j], usuarios_ordenados[j+1] = usuarios_ordenados[j+1], usuarios_ordenados[j]
        
        # Asegurar que el directorio existe
        os.makedirs('data', exist_ok=True)
        
        # Guardar usuarios ordenados en archivo
        with open(OrdenamientoUsuarios.ARCHIVO_ORDENADO, 'wb') as archivo:
            pickle.dump(usuarios_ordenados, archivo)
        
        return usuarios_ordenados