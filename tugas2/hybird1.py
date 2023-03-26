class Pemuda:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

# Single Inheritance

class Mahasiswa(Pemuda):

    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id

    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)

# Single Inheritance

class Santri(Pemuda):
    def __init__(self, name, age, address, santri_id, pesantren):
        super().__init__(name, age, address)
        self.santri_id = santri_id
        self.pesantren = pesantren

    def get_info(self):
        super().get_info()
        print("santri ID:", self.santri_id)
        print("Pesantren:", self.pesantren)

# Multiple Inheritance

class Programmer(Santri, Mahasiswa):
    def __init__(self, name, age, address, santri_id, pesantren, student_id, program_language):
        Santri.__init__(self, name, age, address, santri_id, pesantren)
        Mahasiswa.__init__(self, name, age, address, student_id)
        self.program_language = program_language

    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
        print("Bahasa Pemrogramman:", self.program_language)

