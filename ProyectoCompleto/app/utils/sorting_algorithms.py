from typing import TypeVar, List, Callable

T = TypeVar('T')

class SortingAlgorithms:
    @staticmethod
    def _mostrar_progreso(actual, total, mensaje="Progreso"):
        """Método auxiliar para mostrar progreso de ordenamiento"""
        if actual % 10 == 0:  # Mostrar progreso cada 10 iteraciones
            print(f"{mensaje}: {(actual/total)*100:.1f}%")

    @staticmethod
    def bubble_sort(arr, key_func):
        n = len(arr)
        print("\nProceso de ordenamiento Burbuja:")
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if key_func(arr[j]) > key_func(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            SortingAlgorithms._mostrar_progreso(i, n)
            if not swapped:
                break
        print("Ordenamiento completado!")
        return arr

    @staticmethod
    def selection_sort(arr, key_func):
        n = len(arr)
        print("\nProceso de ordenamiento Selección:")
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if key_func(arr[min_idx]) > key_func(arr[j]):
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            SortingAlgorithms._mostrar_progreso(i, n)
        print("Ordenamiento completado!")
        return arr

    @staticmethod
    def insertion_sort(arr, key_func):
        print("\nProceso de ordenamiento Inserción:")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key_func(key) < key_func(arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            SortingAlgorithms._mostrar_progreso(i, len(arr))
        print("Ordenamiento completado!")
        return arr

    @staticmethod
    def quicksort(arr, key_func, low=None, high=None):
        if low is None:
            low = 0
            high = len(arr) - 1
            print("\nProceso de ordenamiento Quicksort:")

        def partition(low, high):
            i = low - 1
            pivot = key_func(arr[high])
            for j in range(low, high):
                if key_func(arr[j]) <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        if low < high:
            pi = partition(low, high)
            SortingAlgorithms._mostrar_progreso(pi, high, "Procesando partición")
            SortingAlgorithms.quicksort(arr, key_func, low, pi - 1)
            SortingAlgorithms.quicksort(arr, key_func, pi + 1, high)
        
        if low == 0 and high == len(arr) - 1:
            print("Ordenamiento completado!")
        return arr

    @staticmethod
    def sort(arr: List[T], key_func: Callable[[T], any], method: str = 'quick') -> List[T]:
        """
        Método unificado para ordenamiento
        
        Args:
            arr: Lista a ordenar
            key_func: Función para obtener la clave de ordenamiento
            method: Método de ordenamiento ('bubble', 'selection', 'insertion', 'quick')
        
        Returns:
            Lista ordenada
        """
        methods = {
            'bubble': SortingAlgorithms.bubble_sort,
            'selection': SortingAlgorithms.selection_sort,
            'insertion': SortingAlgorithms.insertion_sort,
            'quick': SortingAlgorithms.quicksort
        }
        
        sort_method = methods.get(method.lower())
        if not sort_method:
            raise ValueError(f"Método de ordenamiento no válido: {method}")
            
        return sort_method(arr.copy(), key_func)