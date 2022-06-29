#!/usr/bin/env python

class Person:

    job_list = [
        "Admin",
        "Finance",
        "Customer Service",
        "Sales",
        "Human Resources",
        "General Management",
        "ITC",
        "Research & Development",
        "Production",
        "Marketing",
        "Legal",
        "Purchasing",
    ]

    def __init__(self):
        self._name = "Nobody"
        self._job = "Unemployed"

    def get_name(self):
        return self._name

    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in Person.job_list:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name,)
    job = property(get_job, set_job)
