# Define alert templates using an array of dictionaries
ALERT_TEMPLATES = [
    {
        'title': '🌊 Flooding Alert 🌊',
        'topic': 'emergency/flooding',
        'sample_data': {
            '📍 Location': '[e.g. Stowmarket, Suffolk]',
            '🕒 Time': '[e.g. February 22, 2025]',
            '❗ Implications': '[e.g. Potential for severe property damage and risk to life]',
            '🏥 Health & Welfare': '[e.g. Move to higher ground, avoid walking or driving through floodwaters]',
            '📢 Advice': '[e.g. Follow evacuation orders and stay tuned to local news for updates]',
            '🛡️ Reassurance': '[e.g. Emergency services are responding. Stay calm and stay safe]',
            '🔌 Practical Implications': '[e.g. Expect disruptions to traffic, power supplies, telephones, and water supplies]',
            '📞 Helpline': '[e.g. For assistance, call the Suffolk emergency helpline at 0345 606 6067]'
        }
    },
    {
        'title': '💥 Terrorist Threat Alert 💥',
        'topic': 'emergency/terrorist_threat',
        'sample_data': {
            '📍 Location': '[e.g. Colchester, Essex]',
            '🕒 Time': '[e.g. February 19, 2025]',
            '❗ Implications': '[e.g. Potential for severe injury and loss of life]',
            '🏥 Health & Welfare': '[e.g. Avoid the area, stay indoors, and follow instructions from authorities]',
            '📢 Advice': '[e.g. Report any suspicious activity to the police immediately. Do not spread rumors]',
            '🛡️ Reassurance': '[e.g. Law enforcement is actively responding. Stay vigilant and stay safe]',
            '🔌 Practical Implications': '[e.g. Expect heightened security measures and possible disruptions to public transport]',
            '📞 Helpline': '[e.g. For assistance, call the Essex emergency helpline at 0345 603 7630]'
        }
    },
    {
        'title': '🦠 Public Health Emergency Alert 🦠',
        'topic': 'emergency/public_health',
        'sample_data': {
            '📍 Location': '[e.g. Ipswich, Suffolk]',
            '🕒 Time': '[e.g. Immediate]',
            '❗ Implications': '[e.g. Potential for widespread illness and health complications]',
            '🏥 Health & Welfare': '[e.g. Follow health guidelines, wear masks, and maintain social distancing]',
            '📢 Advice': '[e.g. Avoid large gatherings, wash hands frequently, and stay informed through official channels]',
            '🛡️ Reassurance': '[e.g. Health authorities are managing the situation. Stay informed and stay safe]',
            '🔌 Practical Implications': '[e.g. Expect disruptions to public services and healthcare facilities]',
            '📞 Helpline': '[e.g. For assistance, call the Essex health emergency helpline at 0300 303 9988]'
        }
    },
    {
        'title': '☢️ Nuclear Emergency Alert ☢️',
        'topic': 'emergency/nuclear_war',
        'sample_data': {
            '📍 Location': '[e.g. Suffolk, Essex]',
            '🕒 Time': '[e.g. Immediate]',
            '❗ Implications': '[e.g. Nuclear blast followed by firestorms, radiation and fallout]',
            '🏥 Health & Welfare': '[e.g. Stay indoors, close all windows, stockpile non-perishables and water]',
            '📢 Advice': '[e.g. Tune your radio or TV to the BBC, and await further instructions]',
            '🛡️ Reassurance': '[e.g. The county\'s emergency responders and civil defense forces have been mobilised]',
            '🔌 Practical Implications': '[e.g. Expect disruptions to all public services and utilities for the foreseeable future]',
            '📞 Helpline': '[e.g. For assistance, call the Essex civil defense helpline at 0300 303 9989]'
        }
    }
]