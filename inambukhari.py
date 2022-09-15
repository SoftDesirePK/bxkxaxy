import streamlit as st
import streamlit_authenticator as stauth
# Import the os module
import os
import yaml
from PIL import Image

# --- PATH SETTINGS ---
css_file = "./styles/main.css"
resume_file = "./assets/CV.pdf"
profile_pic = "./assets/profile-pic.png"



st.set_page_config(
    page_title="Inam's Digital CV",
    page_icon="📝",
    layout="wide",
)

## Hide hamburger
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Inam Bukhari"
#PAGE_ICON = ":wave:" 
PAGE_ICON = "🚀"
NAME = "Inam Bukhari! "
DESCRIPTION = """
Technology Advisor, assisting enterprises by supporting data-driven decision-making and by buidling the necessary underlying Big Data infrastructure.
"""
EMAIL = "inambukhari@email.com"


# --- HERO SECTION ---
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    #st.download_button(label=" 📄 Download Resume",data=PDFbyte,file_name=resume_file.name,mime="application/octet-stream",)
    st.write(":e-mail:", EMAIL, " 📞+966 54 00 33 213" )
    st.write(f"📝 [Blog](http://dbmentors.blogspot.com/)", f":large_blue_circle: [Linkedin](https://www.linkedin.com/in/bukhary/)", f":large_blue_diamond: [Twitter](https://twitter.com/BukhariInam)")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')

tabQualification, tabExperience, tabSkills, tabWorkHistory,tabProjects = st.tabs(["Qulifications", "Experience", "Skills","Work History","Projects"])

# 1: -- QUALIFICATION ---
with tabQualification:
     col1, col2= st.columns(2, gap="small")
     with col1:
        st.write(
    """
    ###### 🎓 Academics
- ✔️ **MS Computer Science** - Newports Institute of Communications & Economics

###### 🔖 Self-paced Certifications
- ✔️ Big Data University Certification on Introduction to **Data Analysis using R**
- ✔️ DataCamp Certification on **Data Analysis and Statistical Inference**
- ✔️ DataCamp Certification on Intro to **Statistics with R**
- ✔️ 5-Day **Digital Business Tranformation** Challenge
- ✔️ Congnitive Class - **Blockchain Essentials**
- ✔️ Dremio University - **Dremio Fundamentals**
- ✔️ Dremio University - **Dremio Reflections**
- ✔️ Dremio University - **Dremio for Data Consumers**
- ✔️ MongoDB University- **MongoDB for DBAs**
- ✔️ Virtual University of Pakistan Certification on **Data Warehousing**
- ✔️ Brain Bench Certification on **Oracle PL/SQL**
- ✔️ Brain Bench Certification on **Oracle Forms** 6.0
- ✔️ Brain Bench Certification on **Master Oracle Developer 2000**
- ✔️ Brain Bench Certification on *RDBMS Concepts*
- ✔️ NICON Pakistan Certification on **Oracle Developer & Visual Basic**
"""
)
     with col2:
        st.write(
    """
     ###### 🏅 Industry Standard Certifications
- ✔️ **TOGAF** 9 The Open Group Certified
- ✔️ **PMP** Project Management Professional
- ✔️ Oracle Database 11gR2: **Real Applications Clusters Administrator** Certified Expert
- ✔️ Oracle Certified Professional **Database Administrator Oracle 11g**, Oracle 10g & Oracle 8i
- ✔️ Oracle **E-Business Suite R12 Applications Database Administrator** Certified Professional
- ✔️ Oracle Certified Professional **Database Developer** Release 2.0
- ✔️ Oracle Certified Professional **Internet Application Developer** 6/6i
- ✔️ Sun Certified **Programmer for the Java** 2 Platform
- ✔️ Solution **Consultant mySAP Financials** Managerial and Financial Accounting (2003)

###### 📚 Trainings
- ✔️ EMC  **Data Science and Big Data Analytics**  (*Germany*)
- ✔️ DatascienceDojo  **Machine Learning** (*USA*)
- ✔️ Administering Microsoft SQL Server Databases (*UK*)
- ✔️ **Redhat Openshift** I: Containsers & Kubernetes (*KSA*)
- ✔️ Business Process Redesigned (*KSA*)
- ✔️ IBM Optim Test Data Management (*KSA*)
- ✔️ Information Security Management System (**ITSM**) - SGS *Pakistan*



    """
        )

# 2: -- EXPERIENCE --- :pushpin:
with tabExperience:
    st.write(
    """
    **Summary** 
    - :pushpin: Analytical and results driven IT Consultant/SME with 22+ years of experience in implementing and supporting disaster recovery, high availability and data transformation plans and solutions based on Oracle and Big Data technologies.
    - :pushpin: I may help you transform the way your company uses data and ensure architectural design meets the needs of everyone in your company.
    - :pushpin: Worked with Hadoop, Ozone, Spark, Cassandra, Kudu, HBase, Phoenix, Kafka, Cockroach, Yugabyte, StreamSets, Ignite, Logstash, Presto, RStudio and related technologies
    - :pushpin: Facilitated the migration of a legacy databases as hot archive
    - :pushpin: Trained colleagues in Hadoop, Hive, Kudu, StreamSets, Presto
    - :pushpin: Led Enterprise Log Management project (in-house) from concept to product using related big data technologies
    - :pushpin: Integrated various databases (Postgres, SQL Server, Oracle, MySQL, Kudu) providing federated query capabilities to data engineers
    - :pushpin: Built data pipeline to ingest data to HDFS, Ozone and Kafka
    - :pushpin: Used Kafka, StreamSets and Ignite to help developers in building near real time dashboards
    - :pushpin: Built various big data technologies clusters eg; Apache Ignite, Apache Kudu, Kafka, Hadoop, Presto
    - :pushpin: Worked with Oracle Versions Oracle 7/8/8i/9i/10g/11g/12c
    - :pushpin: Extensive skills in design, installation, and administration upgrade and support of Oracle Databases.
    - :pushpin: RAC Management: Installation, Adding Nodes, unpinning and dropping faulty Nodes, RMAN Backups, Tuning of RAC Database, Administration of RAC and ASM instances, troubleshooting of Local, Virtual IPs, Local and remote (SCAN) listeners, troubleshooting connectivity, ASM storage configuration and management, adding, dropping disk groups to ASM.
    - :pushpin: Database conversion from a single instance to RAC.
    - :pushpin: Disaster recovery plan creation and implementation using Physical Standby with Maximum Protection mode. Database daily, weekly and Monthly hot and cold backups using RMAN, export. RMAN Scripting, RMAN Catalog Management. Automation of RMAN backups using unix cron and Oracle jobs.
    - :pushpin: Support to Development team, writing PL/SQL procedures, packages and triggers as per demand of development team.
    - :pushpin: Data Guard setup for all business critical databases and performed switchover and failover operations on demand
    - :pushpin: Installed and cloning of EBusiness Suite R12 on Linux and Windows with Shared Apps TOP, Maintenance using autoconfig, cloning, patching and backup.
    - :pushpin: DR setup without Oracle Data Guard over EMC’s SRDF/A
    - :pushpin: EBS System administration: Working with Users, Datagroups, Menus, Responsibilities, Data Security Policies, Delegated administration, Auditing resources, Flexfields & Folders.
    - :pushpin: Tuning Oracle databases and tuning applications (SQL). Extensive familiarity with Tuning Tools like Oracle Enterprise Manager's (OEM's), SQL analyzer, Statspack and TOAD.
    - :pushpin: Expert in designing and implementing data integration solutions using Oracle Gateways products and customized PL/SQL code. Worked with Oracle GoldenGate 10g for for enabling the replication of data in heterogeneous data environments.
    - :pushpin: Setting up complete virtualized environment for Oracle Exadata for company’s employees’ learning
    - :pushpin: Experience in Oracle Application Server 10g installation and administration, Oracle Weblogic 11g installation to be used for Oracle Forms & Reports 11g.
    - :pushpin: Expert in Oracle Forms, Reports client server & three tier architecture development using Oracle Developer 2000/Internet Developer Suite 9i & 10g.
    - :pushpin: Experienced in Oracle Portal Development (10g AS), publishing portlets and developing web based reports, using PL/SQL web toolkit and Oracle Intermedia.
    - :pushpin: Experienced in supporting large development teams of 3Involved in complete life cycle of projects including projects of large databases performed systems analysis, design and implementation and maintenance.
    - :pushpin: 0+ developers, working on different technologies i.e., J2EE, Oracle Developer, Oracle iDS, ASP, JSP etc.
    - :pushpin: Delivered lectures on Oracle in various universities and colleges (Pakistan).

    """
    )


# 3: -- SKILLS
with tabSkills:
    tabBigdata, tabOthers = st.tabs(["Big Data", "Others"])
    with tabBigdata:
        col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        st.write(
        """
        ###### 💾 Storage
        - Hadoop/HDFS
        - ORC
        - Parquet
        - Iceberg
        - Minio
        - Ozone
       ###### 👨🏻‍💻 Streaming/Integrations/Data Transfer
        - Flume
        - Kafka
        - Logstash
        - Streamsets DC
        - Beats Framework
        - Fluentbit
        - Fluentd
        - Confluent
        - Sqoop
        - Polybase
        - Alluxio
        - Flink
        - Debezium

        """
        )

    with col2:
        st.write(
        """
        ###### 🖥 Data Warehouse/Data Stores
        - Hive
        - HBase
        - Kudu
        - Cassandra
        - Cockroach DB
        - YugabyteDB
       ###### ⚡ In-Memory Processing
        - Spark
        - Ignite
        ###### 🔍 Search Engines
        - Solr
        - Elastic
        - Opensearch

        ###### 📄 Scripts
        - Linux Shell
        - Python
        - R

        """
        )
    with col3:
        st.write(
        """
        ###### ⚙ SQL Processing
        - TEZ
        - Presto
        - Trino
        - Spark SQL
        - Phoenix
        - 

        ###### 📊BI/UI
        - Zeppelin
        - Superset
        - PowerBI
        - Streamlit



        ###### ⚙️ Machine Learning
        - Quantitative analysis
        - Statistical modeling analysis
        - Data mining and modeling
        - Time series Forecast (Prophet API)


     
        """
        )
    with col4:
        st.write(
        """
        ###### 🛡️ Management/Security/Governance
        - Oozie
        - Ranger
        - Atlas
        - Ambari
        - Zookeeper
        - 
        ###### 🌐 Universal Semantic Layer
        - Dremio
       ###### 📈 Digital/Web Analytics
        - Matomo
        """
        )

    with tabOthers:
        col1, col2, col3 = st.columns(3, gap="small")
        with col1:
            st.write(
        """
        ###### 🖥 RDBMS
        - Oracle Database 11g/10g/9i/8i/8/7
        - Oracle EBS R12
        - MS SQL Server
        - MS Access
        - MySQL
        - Postgres
        ###### 📀 Backups
        - RMAN
        - Data Pump
        - Netbackup
        - Avamar
        - Custom shell scripts
        ###### 📅 Project Management
        - Microsoft Office Project 
        ###### 🌎 Web Technology Tools
        - HTML, JSP/Servlets
        - Python/Streamlit

        """
        )
    with col2:
            st.write(
        """

         ###### ⚒️ Tools/Utilities
         - Oracle 10g Grid Control
         - OEM
         - DBA Studio
         - Server Manager
         - TKProf
         - ExplainPlan
         - STATSPACK
         - SQL* Loader
         - SQL Navigator
         - TOAD/SQuirrel/DBeaver
         ###### ✳️ ERP
         - Oracle EBusiness suite R12 (System Administration)
         - mySAP (Financials & Accounting)
         ###### 🗜️ Modeling/Architecture
         - ErWin
         - UML
         - TOGAF 9
    
        """
        )
    with col3:
            st.write(
       """
         ###### 🧮 Languages
         - Oracle Developer 2000/6i
         - SQL
         - PL/SQL
         - Java
         - Visual Basic
         - C#
         ###### 💻 Operating Systems
         - Windows
         - Linux Redhat
         - CentOS
         - Solaris
         ###### 📱 Virtualization Tools
         - Oracle Virtual Machine
         - VMWare WorkStation 
         ###### 📶 Network
        - TCP/IP,UDP
        - SQL*Net,OCI
        - JDBC, ODBC

        """
        )
# 4: --- Work History ----
with tabWorkHistory:
    tab1, tab2, tab3, tab4,tab5,tab6,tab7 = st.tabs(["[Aug–2021 - Current]", "[Feb -2014 to Aug - 2021]", "[Dec-2007 to Jan 2014]", "[Jun-2005 to Nov-2007]", 
    "[May-2003 to May-2005]", "[Feb 2004 – Aug 2004]", "[Feb-2000 to May-2003]"     ])
    with tab1:
        st.write(
    """
    ###### AEC SAMI/STC Solutions    -   Technology Advisor (https://www.aecl.com/en/)
    - Being part of one of the Kingdom's prestigious Ministry's Deputy Minister’s core team, assisting resources to transform business, organization and culture through the use of modern digital technologies
    - Design, deliver, and manage digital transformation and organization change and culture consulting engagements.
    - Own engagements to inspire decision makers to work with organization teams for their business and culture transformation programs
    - Facilitate change and culture related workshops and training sessions.
    - Design, develop, and deliver training and enablement on digital transformation approaches, methodologies, and best practices for internal teams and partners
    """

    )

    with tab2:
        st.write(
    """
    ###### ELM Information Security    -   Senior Technical Architect/Big Data Subject Matter Expert (www.elm.sa)
-  Part of Project Management Team for Operations department, responsible for the planning, management and coordination of the projects.
-  Part of architectural team responsible for choosing, designing, and deploying strategic software applications, operations, and hardware design, to keep the company’s infrastructure on the leading edge of technology.  Developing company’s IT Disaster Recovery plans, templates and documents for optimal service restoration.
-  Work hand-to-hand with Audit and IT Security to make sure applications are compliant free and safe.
-  Implementing company policies, standards, changes in operation, and systems that optimize productivity and bottom line.
-  Motivating staff to maximum productivity and control costs through the most effective uses of work force and available resources.
-  Managing war rooms during major incidents, taking technical lead to direct internal resources and agreeing action plan with service providers
-  Providing advice on the technical aspects of the projects.
-  Adapting innovations in IT being self-directed and motivated to exceed all targets.
-  Articulating and implementing best practices related to technologies used in various production environments.
-  Defining business requirements and recommending a technical approach to meet those needs.
-  Overseeing the development, testing and implementation of the technical solutions and validating that the final product satisfies the defined requirements.
-  Preparing, reviewing technical documentations prior to distribution to end-users and ensuring that subject area is accurately represented.
-  Cultivating and maintaining effective working relationships with a variety of stakeholders, including project managers, engineers and senior staff members.
-  Actively participating in multiple work-groups (Application, Database, and Infrastructure) at one time and disseminating information across all levels of Operations department.
-  Developed Recovery Planning templates and procedures for Operations
-  Solution Design review for the services to be offered
-  Building Service Maps for the services offered by company
-  Managing teams of DBAs (Oracle and SQLServer).
-  Participating in designing database structure, data transfer procedures and Backup strategy.
-  Managed the Exadata production environments
-  Provide consultation on performance; monitor and tune growth of the database and operating environment
-  Design, implement and maintain most cost effective and efficient solution for Disaster Recovery (DR).
-  Led in-house Log Management project based on Big Data technologies in Operations
-  Integrated all required company’s data sources to big data platform
-  Provided federated query mechanism to data engineers to carry out their daily jobs easily
-  Developed big data batch/cron jobs using R and Shell scripts
-  Deployed and configured various big data technologies’ clusters (Hadoop, Kudu, Kafka, Ignite, Presto)
-  Developed data pipelines for data-on-rest and real time dashboards
-  Parsed and transformed operations’ unstructured data
    """

    )

    with tab3:
        st.write(
    """
    ###### EJADA Systems    -   Senior Oracle Consultant (http://www.ejada.com)
    Client : **Ministry of Higher Education**, Saudi Arabia – (www.mohe.gov.sa) \n
    Software/Applications: Windows 2008R2, Oracle RAC 11g Release 2, PL/SQL Developer, Oracle Application Server, Oracle Weblogic 11g, Oracle Developer 11g, EBS R12, Data Guard, ASM
    \n 
    *Prime Responsibilities*\n

    - Managing a team of developers, system administrator and database administrator.
    - Participated in designing Software Application, database structure, data transfer procedures and Backup strategy.
    - Formulate and implement the backup & recovery strategy keeping in view the business and technical requirements of the system
    - Installed and configured Oracle RAC 11gR2 on Windows and Linux boxes
    - Monitoring using EM, TOAD and Spotlight
    - Installation and configuration of Oracle Database Gateway for MSSQL.
    - Installed and configured Oracle GoldenGate 10g for a POC. POC worked for Oracle to Oracle and Oracle to SQL Server replication.
    - Provide consultation on performance; monitor and tune growth of the database and operating environment
    - Designed and maintained Oracle Application user and system’s security
    - Provide consultation on Clone Apps Environment; Apply Patches to O/S, Apps, Databases, Application Servers
    - Identify innovations and advancements in software and technology that can enhance the efficiency, functionality, distributed nature, performance, and cost of maintaining the new production environment
    - Design, implement and maintain most cost effective and efficient solution for Disaster Recovery(DR).
    - Examine industry trends and new technology; identify architectural challenges and possible future enhancements.
    
    Client : **Saudi Telecom Company (STC)**, Saudi Arabia – (www.stc.com.sa)
    Software/Applications: Red Hat Enterprise Linux Server Version 5, Oracle RAC 10g Release 2, PL/SQL Developer, Oracle Weblogic 10g, ASM, Oracle EBS R12
    \n 
    *Prime Responsibilities*\n
    - Supported QA and Development teams in Performance, Volume and Stress tests, implementing business logic in server side PL/SQL code etc. also transferred knowledge about various new features of oracle 10g and upcoming versions.
    - Installed and configured Oracle RAC 10gR2 on ASM on Red Hat Server.
    - Installed Oracle EBS R12 on Windows 2008.
    - Planned, implemented and maintained a solid backup / recovery procedures using RMAN.
    - Designed complex views & materialized views for the applications
    - Designed, implemented and maintained procedures, automated reporting procedures using Oracle SQL and PL/SQL routines.
    - Performed Database normalization according to RDBMS Techniques for various modules.
    - Developed PL/SQL Packages for EIP Cron jobs which were written in Java. Packages were translated to PL/SQL

    Client : **General Intelligence Presidency (GIP)**, Saudi Arabia – (http://www.gip.gov.sa)
    Software/Applications: Red Hat Enterprise Linux Server Version 5, Oracle RAC 10g Release 2, PL/SQL Developer, Oracle Application Server 10gR2, ASM
    \n 
    *Prime Responsibilities*\n
    - Installed and configured Oracle RAC 10gR2 on ASM on Red Hat Server for GIP portal.
    - Installed and configured Oracle Application Server 10gR2
    - Applied upgrades patches for Oracle AS 10gR2 from 10.1.2 to 10.1.4
    - Planned, implemented and maintained a solid backup / recovery procedures using RMAN.
    - Designed views for GIP portal’s portlets
    - Designed, implemented and maintained procedures, automated reporting procedures using Oracle SQL and PL/SQL routines.
    - Automated email mechanism by Oracle Database
    - Configuration of Oracle Intermedia for handling rich contents for Oracle Portal
    - Integration of Outlook web access with Oracle Portal.
    - Configured Windows Native Authentication with Microsoft Exchange
    - Helped development team to Develop different portlets with PL/SQL web toolkit and PSP
    - LDAP integration with Oracle Portal
    - Configured Oracle Portal’s Omni, HTML and administrative portlets
    - Managing (Configuration, Deployment, Maintenance )the Production Server remotely using SSH.
    - Developed proof of concept for Oracle Webcenter
    
    Client : **Ministry of Interior (MOI)**, Saudi Arabia – (http://www.moi.gov.sa)
    Software/Applications: Microsoft Windows Server 2008R2, Oracle RAC 11g Release 2, PL/SQL Developer, ASM,GIS
    \n 
    *Prime Responsibilities*\n
    - Installed and configured 6 Oracle clusters 11gR2 on Windows Server 2008 for GIS databases.
    - Maintained 10gR2 cluster on Windows 2008.
    - Migrated GIS databases to newly built clusters
    - Developed Backup strategies for newly built RACs.
    - Troubleshooting database and cluster issues on demand.
   """

    )

    with tab4:
        st.write(
    """
    ###### NetSol Technologies Limited , Pakistan    -   Software Architect (www.netsolpk.com)
    Client : **State Bank of Pakistan** – (http://www.sbp.org.pk/) \n
    Software/Applications: Oracle 8i/9i/10g databases, Oracle Developer 9i/10gR2 \n
    *Prime Responsibilities* \n
    - Involved in Business process analysis for Electronic Credit Information Bureau, developed design documents for the projects.
    - Gathered requirements and wrote requirement/functional specifications
    - Installed and configured Oracle Databases for various applications.
    - Installed and configured Oracle Application Server 10gR2 with webutil
    - Served on an end-to-end implementation, upgrade or improvement project from assessment to production support as the primary DBA for key Oracle databases and services of the company’s enterprise application platform
    - Setup and maintained reporting infrastructure
    - Database performance tuning and monitoring; data migration, user and system security, database cloning, capacity and space management, problem resolution,, system documentation, and system management and support on a day to day basis
    - Accountable for proper backup and disaster recovery procedures
    - Configured the policies for Oracle Private Database.
    - Maintain production database via VPN remotely.
    - Responsible for applying patches to, databases, custom application
    - Trained the business users on the functional aspects.
    - Trained the technical users on maintenance and administration of database, network and OS etc.
    - Lead the Back Office team.
    Client : **MTMIS Govt. of Punjab**, Pakistan – ( http://mtmis.punjab.gov.pk/)  
    *Prime Responsibilities* \n
    - Installed and configured Oracle Databases for the applications running in various districts of province of Punjab.
    - Migrated Oracle 8 database to Oracle 9i.
    - Developed TOAD, SQL*loader scripts to load data in the custom tables.
    - Designed and developed Oracle logical backup mechanism in the application itself with the help of java stored procedures.
    - Tuned various oracle server structures i.e. Shared pool, Data buffer and log cache for optimal performance.
    - Implemented Multi-Threaded Server architecture for optimal resource utilization.
    - Implemented data loading schemes using SQL Loader from various data sources.
    - Developed PL/SQL routines for different modules of application.
    - Configure the Oracle replication.
    - Managed the MTMIS (Motor Transport Management Information System) project after first implementation as Project lead.
    
    Client :**General Head Quarter Pak Army**, Pakistan    
    *Prime Responsibilities* \n
    - Analyzed Functional requirements by interacting with users and creating design & technical documents for GHQ’s Office Automation System (GOAS) aimed to automate all the workings of Pakistan Army General Head Quarters, Rawalpindi, Pakistan.
    - Installed Oracle Database 10g for the project, developed backup and recovery strategies.
    - Performed research activities for FileNet P8 plat form and delivered to resources working on project.
    - LDAP configuration with BEA Weblogic portal.
    - Developed data models for various components of the project.
    
    Client : **Pakistan Military Academy** Kakool, Pakistan
    *Prime Responsibilities* \n
    - Requirement gathering activity for the custom ERP project consisting of 30 moduels.
    - Requirement specification, functional specification, use case modeling, database modeling
    - Installed Oracle 10g, schema creation as per the database modeling
    - Configure Streaming Services Media 9 for project’s Multimedia module



    """
    )


    with tab5:
        st.write(
    """
    ###### Railways Head Quarter Office, Pakistan    -   Senior Programmer BPS-17 (http://pakrail.com)
    Software/Applications: Oracle 8i database running on Digital Server on MS Windows NT 4.0. Application written
    in JAM & Oracle Develper iDS 9i \n
    *Prime Responsibilities* \n
    - Worked as a senior programmer for various applications using Oracle PL/SQL and iDS. Applications include \n
        o Reservation and Ticketing \n
        o Cancellation and Waiting \n
        o Train Generation \n
        o Fare Management \n
        o Reserved and Availability Status \n
        o Application Portal \n
        o Pension System \n
        o Personnel System \n
    - Supported as database administrator also.
    - Installed Oracle Databases and Application Server on Red Hat.
    - Configured Samba server on RedHat Linux.



    """

    )

    with tab6:
        st.write(
    """
    ###### BORJAN , Dyal Singh Mansion Lahore, Pakistan    -   Database Consultant – part time (https://www.borjan.com.pk/)
    Software/Applications: Oracle 8 database, Oracle Developer 2000
    *Prime Responsibilities* \n

    - Assisted Borjan developers as Database consultant for their new applications
    - Developed few complex PL/SQL routines.
    - Training to Borjan employees regarding DB administration.
    - Troubleshoot day to day problems.
    """

    )

    with tab7:
        st.write(
    """
    ###### NKFACT College Pakistan    -   Lecturer 
    *Prime Responsibilities* \n

    - Delivery of appropriate and approved computer lessons for BCS & MCS as Oracle instructor.
    - Developed training curriculums, materials and exercises for students.
    - Conducted Oracle Certification program for Oracle Developer and DBA tracks.
    - Assist students in their final database projects.
    """

    )
       
        







