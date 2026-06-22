from flask import Flask, render_template, jsonify
import os
# Get the absolute path of the directory containing api/index.py, then go up one level to the root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static'),
    static_url_path='/static' # Explicitly tells Flask to match your vercel.json static route
)

PROJECTS = [
    {
        "id": 1,
        "title": "Sports Ground Reservation System",
        "category": "fullstack",
        "tag": "Full-Stack",
        "description": "Real-time booking platform for sports facilities. Features live availability tracking, user authentication, and security hardening against XSS, CSRF and SQL injection.",
        "tech": ["PHP", "Symfony", "MySQL", "HTML/CSS", "JavaScript"],
        "github": "https://github.com/Mariem20abdelhak/ReservationTerrain",
        "live": None,
        "highlight": "Security-hardened with protection against common web attacks"
    },
    
    {
        "id": 2,
        "title": "Dynamic E-Commerce Platform",
        "category": "web",
        "tag": "E-Commerce",
        "description": "Full e-commerce website built from scratch with product and customer database management, intuitive UX, and real-time stock management system.",
        "tech": ["PHP", "MySQL", "Bootstrap"],
        "github": "https://github.com/Mariem20abdelhak/quincaillerie",
        "live": None,
        "highlight": "Real-time inventory and seamless purchasing experience"
    },
    {
        "id": 3,
        "title": "Network Security Labs",
        "category": "security",
        "tag": "Cybersecurity",
        "description": "Hands-on labs using Cisco Packet Tracer and Wireshark for network topology simulation, traffic analysis, and vulnerability assessment exercises.",
        "tech": ["Cisco Packet Tracer", "Wireshark", "Linux", "Python"],
        "github": "https://github.com/Mariem20abdelhak",
        "live": None,
        "highlight": "Network traffic analysis and vulnerability assessment"
    },
    {
        "id": 4,
        "title": "OneClick — WinDev Applications",
        "category": "fullstack",
        "tag": "Desktop + Web",
        "description": "Production desktop applications built with WinDev. Includes database design, UI/backend integration, access control, and security hardening for business clients.",
        "tech": ["WinDev", "WebDev", "SQL", "HyperFileSQL"],
        "github": "https://github.com/Mariem20abdelhak",
        "live": None,
        "highlight": "Business-grade access control and security hardening"
    },
    {
        "id": 5,
        "title": "Camera Inspection System",
        "category": "industrial",
        "tag": "Industrial",
        "description": "Automated visual inspection system for production line quality control at Rosenberger. Reduced line downtime via optimized maintenance processes and equipment parameter management.",
        "tech": ["Siemens", "ZU-Vision", "INSIGHT", "MSA Analysis"],
        "github": "https://github.com/Mariem20abdelhak",
        "live": None,
        "highlight": "Reduced production downtime through automation"
    },
    {
        "id": 6,
        "title": "IT asset manager",
        "category": "fullstack",
        "tag": "Full-Stack",
        "description": "signed and developed a full IT asset management system using the Odoo framework.",
        "tech": ["Python", "Odoo", "PostgreSQL", "XML"],
        "github": "https://github.com/Mariem20abdelhak/Odoo-it-asset-manager",
        "live": None,
        "highlight": "Implemented Python backend logic, XML views, and automated workflows for asset status updates and alerts."
    },
]

EXPERIENCE = [
    {
        "role": "Full-Stack Software Developer",
        "company": "OneClick",
        "location": "Al Munastir, Tunisia",
        "period": "April 2026 — Present",
        "current": True,
        "bullets": [
            "Develop desktop & web applications using WinDev and WebDev",
            "Design relational database schemas and optimize SQL queries",
            "Apply security best practices: input validation, access control, authentication",
            "Participate in agile sprints, code reviews, and technical documentation",
        ]
    },
    {
        "role": "Technical Support Technician (SAV)",
        "company": "Takiacademy",
        "location": "Sousse, Tunisia",
        "period": "May 2025 — March 2026",
        "current": False,
        "bullets": [
            "Diagnosed and resolved hardware, software, and network issues",
            "Delivered remote preventive and corrective maintenance",
            "Trained users to optimize the use of IT tools and platforms",
        ]
    },
    {
        "role": "Process Technician",
        "company": "Rosenberger",
        "location": "Enfidha Industrial Zone",
        "period": "August 2023 — March 2025",
        "current": False,
        "bullets": [
            "Created camera inspection systems for production quality control",
            "Reduced line downtime through optimized maintenance workflows",
            "Conducted MSA (Measurement System Analysis) on test equipment",
        ]
    },
]

SKILLS = {
    "Languages": ["Python", "Java", "PHP", "HTML/CSS", "JavaScript", "SQL"],
    "Frameworks": ["Spring Boot", "Symfony", "WinDev", "Bootstrap", "Flask"],
    "Databases": ["PostgreSQL", "MySQL", "MongoDB"],
    "Security": ["Wireshark", "Cisco Packet Tracer", "Cybersecurity Basics", "OWASP"],
    "DevOps": ["Git", "GitHub", "Docker", "Linux"],
}

@app.route("/")
def index():
    return render_template("index.html",
        projects=PROJECTS,
        experience=EXPERIENCE,
        skills=SKILLS
    )

@app.route("/api/projects")
def api_projects():
    return jsonify(PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)
