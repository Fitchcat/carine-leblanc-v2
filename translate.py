import os

with open('index_en.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    'lang="fr"': 'lang="en"',
    'Assistante Personnelle': 'Personal Assistant',
    '<a href="#accueil">ACCUEIL</a>': '<a href="#accueil">HOME</a>',
    '<a href="#qui-suis-je">QUI SUIS-JE</a>': '<a href="#qui-suis-je">ABOUT ME</a>',
    '<a href="#mon-approche">MON APPROCHE</a>': '<a href="#mon-approche">MY APPROACH</a>',
    '<a href="#services">MES SERVICES</a>': '<a href="#services">MY SERVICES</a>',
    '<a href="#contact" class="btn">CONTACT</a>': '<a href="#contact" class="btn">CONTACT</a>',
    '<span class="active">FR</span> | <a href="#en">EN</a>': '<a href="index.html">FR</a> | <span class="active">EN</span>',
    'Moins de contraintes': 'Less constraints',
    "Plus de temps pour l'essentiel": 'More time for what matters',
    "J'accompagne les personnes très occupées en prenant en charge leurs tâches chronophages, afin qu'elles puissent se concentrer sur ce qui compte vraiment.": "I support busy individuals by taking care of their time-consuming tasks, so they can focus on what truly matters.",
    'SERVICES SUR-MESURE<br>POUR UNE VIE PLUS SIMPLE': 'TAILOR-MADE SERVICES<br>FOR A SIMPLER LIFE',
    'Qui suis-je ?': 'About me',
    'Plus de 17 années d’expérience en assistanat de direction et en gestion immobilière, dont 8 années d’expatriation.': 'Over 17 years of experience in executive assistance and property management, including 8 years as an expatriate.',
    'Réactive, disponible, autonome et consciencieuse, je parle couramment anglais et mets toutes mes compétences au service de votre organisation.': 'Responsive, available, autonomous, and conscientious, I speak fluent English and put all my skills at the service of your organization.',
    'Mon approche': 'My approach',
    'Mon rôle se situe à mi-chemin entre l’assistanat de direction et l’assistanat virtuel, mais avec une approche différente : <strong>humaine, personnalisée et évolutive</strong>.': 'My role sits halfway between executive assistance and virtual assistance, but with a different approach: <strong>human, personalized, and scalable</strong>.',
    'Je rencontre toujours mes clients afin de construire une relation de confiance.': 'I always meet my clients in order to build a relationship of trust.',
    'Cette proximité me permet d’intervenir sur des aspects professionnels (séminaires, livraisons de véhicules, agenda, déplacements) mais aussi personnels (rendez-vous médicaux, intendance maison, gestion de résidence secondaire, organisation de vacances).': 'This proximity allows me to intervene in professional aspects (seminars, vehicle deliveries, schedule management, business travel) as well as personal ones (medical appointments, home management, second home management, vacation planning).',
    'Avec moi, la collaboration s’adapte à vos besoins et évolue avec le temps.': 'With me, the collaboration adapts to your needs and evolves over time.',
    'MES VALEURS': 'MY VALUES',
    '<h3>CONFIANCE</h3>': '<h3>TRUST</h3>',
    '<h3>RÉACTIVITÉ</h3>': '<h3>RESPONSIVENESS</h3>',
    '<h3>DISPONIBILITÉ</h3>': '<h3>AVAILABILITY</h3>',
    '<h3>DISCRÉTION</h3>': '<h3>DISCRETION</h3>',
    '<h3>QUOTIDIEN</h3>': '<h3>DAILY LIFE</h3>',
    'Aide administrative': 'Administrative support',
    'Recherche de prestataires': 'Finding service providers',
    'Gestion de budget': 'Budget management',
    'Livraison (courses, pressing)': 'Deliveries (groceries, dry cleaning)',
    'RDV médicaux': 'Medical appointments',
    'Entretien immobilier': 'Property maintenance',
    '<h3>ÉVÉNEMENTS</h3>': '<h3>EVENTS</h3>',
    'Traitement du courrier': 'Mail handling',
    'Planification & Agenda': 'Scheduling & Calendar',
    'Déplacements professionnels': 'Business travel',
    'Séminaires événementiels': 'Event seminars',
    'Services généraux': 'General services',
    'Réservations (taxi, hôtel...)': 'Bookings (taxi, hotel...)',
    '<h3>LOISIRS</h3>': '<h3>LEISURE</h3>',
    'Organisation de voyages': 'Travel organization',
    'Billetterie (transport, cinéma)': 'Ticketing (transport, cinema)',
    'Recherche de coach sportif': 'Finding a sports coach',
    'Professeur particulier': 'Private tutor',
    'Réservations loisirs': 'Leisure bookings',
    '<h3>RELOCATION</h3>': '<h3>RELOCATION</h3>',
    'Recherche de logement': 'Housing search',
    'Agences immobilières': 'Real estate agencies',
    "Recherche d'école": 'School search',
    'Déménagement': 'Moving',
    "Transfert d'abonnements": 'Subscription transfers',
    'Une demande ? Un besoin ?': 'A request? A need?',
    "N'hésitez pas à me contacter pour toute demande d'information ou devis.": 'Do not hesitate to contact me for any information request or quote.',
    'ME CONTACTER': 'CONTACT ME',
    'Tous droits réservés.': 'All rights reserved.'
}

for k, v in replacements.items():
    html = html.replace(k, v)

with open('index_en.html', 'w', encoding='utf-8') as f:
    f.write(html)
