import streamlit as st

# Configuração da página
st.set_page_config(page_title="Currículo Márcio Brufatto", page_icon="📄", layout="centered")

# Adicionar seleção de idioma
st.sidebar.title("🌐 Selecione o Idioma / Language")
language = st.sidebar.radio("Escolha um idioma / Choose a language:", ("🇧🇷 Português", "🇺🇸 English"))

# Função para currículo em Português
def show_curriculo_pt():
    # Layout com colunas: Texto do endereço (esquerda) e imagem (direita)
    col1, col2 = st.columns([3, 1])  # A coluna 1 tem 3 partes do espaço, a coluna 2 tem 1 parte
    
    with col1:
        st.title("Márcio H. Brufatto")
        st.write("Brasileiro, solteiro, 42 anos  \nFlorianópolis – SC  \n**Telefone:** (51) 98461-9504  \n**E-mail:** mhbrufatto@gmail.com")
    
    with col2:
        st.image("foto.png", width=150, caption="Márcio H. Brufatto")  # Ajuste o nome e caminho da imagem

    st.header("Resumo")
    st.write("""
    Sou Márcio Brufatto, desenvolvedor de software com mais de 13 anos de experiência, especializado em iOS desde o lançamento do iPhone 4. Durante minha trajetória, tive a oportunidade de trabalhar em empresas como uMov.me, Makadu, Zup Innovation, Act Digital e TIVIT, onde desenvolvi e mantive aplicativos móveis para grandes bancos, além de contribuir em outros projetos importantes. Também possuo experiência em desenvolvimento web, com foco em Python e PostgreSQL, e sou empreendedor — fundei a DeliveryVeg em 2014. Atualmente, estou cursando uma pós-graduação em Inteligência Artificial na FIAP e me dedicando aos estudos de SwiftUI e IA. Tenho ainda um histórico ativo em comunidades de tecnologia, destacando minha atuação como coordenador do Grupo de Usuários Mobile do Rio Grande do Sul entre 2016 e 2019.
    """)

    st.header("EXPERIÊNCIA PROFISSIONAL DESTACADA")
    st.write("""
    Atuou em diferentes posições, entregando soluções robustas e eficientes para plataformas móveis e web, destacando:\n\n
             
    - **Zup Innovation (2021-2024):** Desenvolvedor iOS, contribuindo com novos recursos e manutenções para aplicativos 
    bancários e de telecomunicações para as empresas Itaú e Claro.

    - **TIVIT e Act Digital (2021):** Desenvolvimento de soluções mobile utilizando Dart/Flutter, Objective-C e Swift como principal 
    cliente o Banco Santander.

    - **Mantra Tech (2014-2021):** Como fundador, Márcio liderou projetos em múltiplos setores, desenvolvendo soluções para 
    aplicações de e-commerce, controle via Bluetooth e integração com SAP SDK.

    """)

    st.header("EXPERIÊNCIA TÉCNICA")
    st.write("""  
    Possui domínio em linguagens como Swift, Objective-C, Python, Node.js, e em frameworks como Alamofire, UIKit e CoreData. 
    Ele é proficiente em metodologias ágeis e práticas modernas de desenvolvimento, incluindo testes unitários e padrões de 
    arquitetura como MVVM-C.
    """)

    st.header("EMPREENDEDORISMO E COMUNIDADE")
    st.write("""
    Fundador da DeliveryVeg em 2014, ele explorou todos os aspectos de uma jornada empreendedora. Também liderou o Grupo de Usuários 
    Mobile do RS (2016-2019) e participou de eventos como palestrante e coordenador de trilhas no TDC.
    """)

    st.header("EDUCAÇÃO CONTINUADA")
    st.write("""
    - Cursando pós-graduação em Inteligência Artificial (FIAP, 2025).  
    - Graduação em Análise e Desenvolvimento de Software (UNISINOS, 2019).
    - Cursos técnicos em redes de computadores e processamento de dados.
    - Inglês intermediário.
             
    Márcio se destaca por sua paixão pelo aprendizado contínuo, estando atualmente focado em SwiftUI e aplicações de 
    Inteligência Artificial, fortalecendo sua capacidade de criar soluções tecnológicas inovadoras.

    """)

# Função para currículo em Inglês
def show_curriculo_en():
    # Layout com colunas: Texto do endereço (esquerda) e imagem (direita)
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title("Márcio H. Brufatto")
        st.write("Brazilian, single, 42 years old  \nFlorianópolis – SC  \n**Phone:** +55 (51) 98461-9504  \n**Email:** mhbrufatto@gmail.com")
    
    with col2:
        st.image("foto.png", width=150, caption="Márcio H. Brufatto")  # Ajuste o nome e caminho da imagem

    st.header("SUMMARY")
    st.write("""
    I'm Márcio Brufatto, a software developer with over 13 years of experience, specializing in iOS since the launch of the iPhone 4. During my career, I had the opportunity to work at companies such as uMov.me, Makadu, Zup Innovation, Act Digital and TIVIT, where I developed and maintained mobile applications for large banks, in addition to contributing to other important projects. I also have experience in web development, with a focus on Python and PostgreSQL, and I'm an entrepreneur — I founded DeliveryVeg in 2014. I'm currently studying a postgraduate degree in Artificial Intelligence at FIAP and dedicating myself to studying SwiftUI and AI. I also have an active history in technology communities, highlighting my role as coordinator of the Rio Grande do Sul Mobile User Group between 2016 and 2019.
    """)

    st.header("OUTSTANDING PROFESSIONAL EXPERIENCE")
    st.write("""
    He has worked in different positions, delivering robust and efficient solutions for mobile and web platforms, highlighting:\n\n
             
    - **Zup Innovation (2021-2024):** OS Developer, contributing new features and maintenance for banking and telecommunications 
    applications for the companies Itaú and Claro.

    - **TIVIT and Act Digital (2021):** Development of mobile solutions using Dart/Flutter, Objective-C and Swift with the main client 
    being Banco Santander.

    - **Mantra Tech (2014-2021):** As founder, Márcio has led projects in multiple sectors, developing solutions for e-commerce applications, Bluetooth 
    control and integration with SAP SDK.
    """)

    st.header("TECHNICAL EXPERIENCE")
    st.write("""
    He is proficient in languages ​​such as Swift, Objective-C, Python, Node.js, and frameworks such as Alamofire, UIKit, and CoreData. 
    He is proficient in agile methodologies and modern development practices, including unit testing and architectural patterns such as 
    MVVM-C.
    """)

    st.header("ENTREPRENEURSHIP AND COMMUNITY")
    st.write("""
    Founder of DeliveryVeg in 2014, he has explored all aspects of an entrepreneurial journey. 
    He also led the RS Mobile User Group (2016-2019) and participated in events as a speaker and track coordinator at TDC.
    """)

    st.header("CONTINUING EDUCATION")
    st.write("""
    - Studying postgraduate studies in Artificial Intelligence (FIAP, 2025).  
    - Degree in Software Analysis and Development (UNISINOS, 2019).
    - Technical courses in computer networks and data processing.
    - Intermediate English.
             
    Márcio stands out for his passion for continuous learning, currently focusing on SwiftUI and Artificial Intelligence applications, 
    strengthening his ability to create innovative technological solutions.
    """)

# Exibe o currículo com base no idioma selecionado
if language == "🇧🇷 Português":
    show_curriculo_pt()
else:
    show_curriculo_en()

# Rodapé
st.write("**Versão Web do Currículo desenvolvida com ❤️ usando Streamlit!**")
