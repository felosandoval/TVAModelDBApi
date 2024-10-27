from flask_sqlalchemy import SQLAlchemy
#import sqlalchemy

db = SQLAlchemy()
#db = sqlalchemy()

# Modelos ORM

class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    requisito = db.Column(db.String(50), nullable=False)
    fecha_creacion = db.Column(db.Integer, nullable=False)

    @classmethod
    def create(cls, nombre, requisito, fecha_creacion):
        departamento = Departamento(
            nombre=nombre, requisito=requisito, fecha_creacion=fecha_creacion)
        return departamento.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'requisito': self.requisito,
            'fecha_creacion': self.fecha_creacion
        }


# ID-EMPLEADO-, ID-DEP-, N-EMPLEADO-, CARGO-DEP-, F-INGRESO-, F-EMPLEADO
class Empleado(db.Model):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, primary_key=True)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'))
    nombre = db.Column(db.String(50), nullable=False)
    fecha_ingreso = db.Column(db.Integer, nullable=False)
    cargo = db.Column(db.String(50), nullable=False)

    @classmethod
    def create(cls, id_departamento, nombre, fecha_ingreso, cargo):
        empleado = Empleado(nombre=nombre,fecha_ingreso=fecha_ingreso,cargo=cargo)
        return empleado.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'fecha_ingreso': self.fecha_ingreso,
            'cargo': self.cargo
        }


class Jefe_departamento(db.Model):

    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'),  primary_key=True)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleado.id'),  primary_key=True)

    @classmethod
    def create(cls, id_departamento, id_empleado):
        jefe_departamento = Jefe_departamento()
        return jefe_departamento.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def json(self):
        return {
            'id_departamento': self.id_departamento,
            'id_empleado': self.id_empleado,
        }


# ID-VIAJE-, FI-INFORME-, E-VIAJE, DUR-MIS,M-DEPARTAMENTO
class Mision(db.Model):
    __tablename__ = 'mision'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
    departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'))
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id'))

    @classmethod
    def create(cls, id, nombre, duracion, id_empleado):
        mision = Mision(nombre=nombre,duracion=duracion,departamento=departamento,id_empleado=empleado)
        return mision.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'duracion': self.duracion,
            'departamento': self.departamento,
            'id_empleado': self.empleado
        }


# ID-VIAJE,L-TEMPORAL,C-ENERGIA
class Viaje(db.Model):
    __tablename__ = 'viaje'
    id = db.Column(db.Integer, primary_key=True)
    linea_temporal = db.Column(db.String(50), nullable=False)
    variante = db.Column(db.String(15), nullable=False)
    costo_energia = db.Column(db.Integer, nullable=False)
    amenaza= db.Column(db.String(15), nullable=False)
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id'))

    @classmethod
    def create(cls, id, linea_temporal, variante,costo_energia,amenaza, id_empleado):
        viaje = Viaje(linea_temporal=linea_temporal,variante=variante,costo_energia=costo_energia,amenaza=amenaza,id_empleado=id_empleado)
        return mision.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'linea_temporal': self.linea_temporal,
            'variante': self.variante,
            'costo_energia': self.costo_energia,
            'amenaza':self.amenaza,
            'id_empleado': self.id_empleado
        }
