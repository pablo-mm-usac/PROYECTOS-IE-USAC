pkg load database
%Conectamos con la BD
conn = pq_connect (setdbopts ('dbname',"proyectos",'user',"postgres",'password',"202201199"));

N = pq_exec_params (conn, "INSERT INTO REDES VALUES('PEDRO','202201199');")
M = pq_exec_params (conn, "SELECT * FROM REDES;")
