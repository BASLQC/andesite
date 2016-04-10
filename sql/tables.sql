CREATE TABLE Sorite(

  id VARCHAR(5) PRIMARY KEY,
  world_name	TEXT,	
  battle_name	TEXT, 
  stars         INT,  
  position	JSONB

);

CREATE TABLE Ships(

  class_id	FOREIGN KEY, references Class(class_id),
  statistics	JSONB(),
  build_time	TIME,
  equipment	JSONB(),
  ship_ID		INT, PRIMARY KEY
  ship_Name	TIME()
); 

CREATE TABLE Class (

  class_id  VARCHAR(),
  ship_ID FOREIGN KEY references ships(ship_ID),
  info JSONB
  
);

CREATE TABLE Update(
  name	VARCHAR,
  ship_ID FOREIGN KEY references ships(ship_ID),
  info JSONB


);

CREATE TABLE expedition (

  name	VARCHAR()
  time	TIME()
  resources JSONB
  regulated_ships	JSONB
  unlock	INT
  

);

CREATE TABLE equipment(

  name	VARCHAR
  stars INT FK?
  varity	INT
  ships	JSONB  FK?
  statistics	FK
  quest	JSONB	TEXT?

):