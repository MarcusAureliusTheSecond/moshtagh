from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.appointment_date}"

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    medication = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return f"Prescription for {self.appointment.patient.name}"