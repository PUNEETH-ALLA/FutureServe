from django.shortcuts import render

# Home Page View
def home(request):
    return render(request, 'home/index.html')

# Services Page View
def services(request):
    return render(request, 'home/services.html')

# Service Detail Page View
def service_detail(request, service_name):
    services = {
        "it-staffing": {
            "title": "IT Staffing & Consulting",
            "description": "Providing top-tier IT professionals."
        },
        "app-development": {
            "title": "Application Development",
            "description": "Custom software solutions for businesses."
        },
        "tech-support": {
            "title": "Tech Support",
            "description": "Ensuring smooth IT operations for businesses."
        }
    }
    return render(request, 'home/service_detail.html', {"service": services.get(service_name, {"title": "Service Not Found"})})

# Careers Page View
def careers(request):
    return render(request, 'home/careers.html')

# Career Detail Page View
def career_detail(request, job_title):
    jobs = {
        "java-full-stack-developer": {
            "title": "Java Full Stack Developer",
            "location": "Remote",
            "experience": "3+ Years",
            "description": "Develop and maintain full-stack applications using Java, Spring Boot, React.js, and MySQL.",
            "responsibilities": [
                "Develop full-stack web applications.",
                "Ensure best coding practices.",
                "Work in Agile teams."
            ],
            "requirements": [
                "Experience with Java, Spring Boot, React.js.",
                "Understanding of RESTful APIs.",
                "Knowledge of databases like MySQL or PostgreSQL."
            ]
        },
        "machine-learning-engineer": {
            "title": "Machine Learning Engineer",
            "location": "Hybrid",
            "experience": "2+ Years",
            "description": "Develop AI models for predictive analytics and automation.",
            "responsibilities": [
                "Develop AI models using Python and TensorFlow.",
                "Work on cloud AI solutions.",
                "Deploy and maintain ML pipelines."
            ],
            "requirements": [
                "Strong understanding of machine learning concepts.",
                "Experience with Python, TensorFlow, and cloud platforms.",
                "Ability to work on large datasets."
            ]
        }
    }
    job = jobs.get(job_title, {"title": "Job Not Found"})
    return render(request, 'home/career_detail.html', {"job": job})

# Contact Page View
def contact(request):
    return render(request, 'home/contact.html')

# About Page View
def about(request):
    return render(request, 'home/about.html')

# Industries Page View
def industries(request):
    return render(request, 'home/industries.html')
