import unittest
def buscar_datos(*args, **kwargs):
    
    for persona, datos in kwargs.items():
        lista=[]
        for arg in args:
            if arg in datos.values():
                lista.append(arg)
        lista.sort()
        argsOrdenados=list(args)
        argsOrdenados.sort()
        if lista == argsOrdenados and len(lista)==len(datos.values()):
            return persona
       
    return "error"
   
database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Andres",
        "segundo_nombre": "Jesus",
        "primer_apellido": "Pepe",
        "segundo_apellido": "Nose"
    },
    "persona3": {
        "primer_nombre": "Joaquin",
        "segundo_nombre": "Furque",
        "primer_apellido": "Martin",
        "segundo_apellido": "Paez"
    },
    "persona4": {
        "primer_nombre": "Santiago",
        "primer_apellido": "Rodriguez",
        "segundo_apellido": "Gonzales"
    }
}
class TestPalindrome(unittest.TestCase):
    def test_persona1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz","Picasso", **database)
        self.assertEqual(resultado, "persona1")
    def test_persona2(self):
        resultado = buscar_datos("Andres","Jesus","Pepe","Nose", **database)
        self.assertEqual(resultado, "persona2")
    def test_persona3(self):
        resultado = buscar_datos("Joaquin","Furque","Martin","Paez",**database)
        self.assertEqual(resultado, "persona3")
    def test_persona1_con_error(self):
        resultado = buscar_datos("Pablo", "Diego", "Rdfgdgdfdfgdfguiz","Picasso", **database)
        self.assertEqual(resultado, "error")
    def test_persona_que_no_existe(self):
        resultado = buscar_datos("Miguel", "Yudica", "Cristian","aaaa", **database)
        self.assertEqual(resultado, "error")
    def test_persona1_con_menos_parametros(self):
        resultado = buscar_datos("Pablo","Picasso", **database)
        self.assertEqual(resultado, "error")
    def test_persona4(self):
        resultado = buscar_datos("Santiago", "Rodriguez", "Gonzales", **database)
        self.assertEqual(resultado, "persona4")
    def test_persona4_sin_parametros(self):
        resultado = buscar_datos("", **database)
        self.assertEqual(resultado, "error")


unittest.main()
