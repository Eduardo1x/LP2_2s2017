agenda = {
    'Alberto':['555-000', '666-000'],
    'Bianca':'555-111',
    'Carlos':['555-222']
}

agenda = {
    'Alberto':{
        'telefone':['555-000', '666-000'],
        'email':'alberto@alberto.com'
    },
    'Bianca':{
        'telefone':'555-111',
    },
    'Carlos':{
        'telefone':['555-222'],
        'email':'carlos@carlos.com'
    }
}

telAlberto = agenda['Alberto']['telefone']
emailCarlos = agenda['Carlos']['email']

