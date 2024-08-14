CREATE TABLE "fact_trip" (
  "trip_id" varchar(50) PRIMARY KEY,
  "rider_id" int,
  "start_station_id" varchar(50),
  "end_station_id" varchar(50),
  "trip_date_id" int,
  "duration" int,
  "rider_age" int
);

CREATE TABLE "fact_payment" (
  "payment_id" int PRIMARY KEY,
  "payment_date_id" int,
  "amount" decimal(10,2),
  "rider_id" int
);

CREATE TABLE "dim_rider" (
  "rider_id" int PRIMARY KEY,
  "first" varchar(50),
  "last" varchar(50),
  "birthday" date,
  "account_start_date" date,
  "age_at_account_start" int,
  "membership_status" varchar(10)
);

CREATE TABLE "dim_date" (
  "date_id" int PRIMARY KEY,
  "date" date,
  "day_of_week" varchar(10),
  "month" int,
  "quarter" int,
  "year" int
);

CREATE TABLE "dim_station" (
  "station_id" varchar(50) PRIMARY KEY,
  "name" varchar(255),
  "latitude" float,
  "longitude" float
);

ALTER TABLE "fact_payment" ADD FOREIGN KEY ("payment_date_id") REFERENCES "dim_date" ("date_id");

ALTER TABLE "fact_payment" ADD FOREIGN KEY ("rider_id") REFERENCES "dim_rider" ("rider_id");

ALTER TABLE "fact_trip" ADD FOREIGN KEY ("trip_date_id") REFERENCES "dim_date" ("date_id");

ALTER TABLE "fact_trip" ADD FOREIGN KEY ("rider_id") REFERENCES "dim_rider" ("rider_id");

ALTER TABLE "fact_trip" ADD FOREIGN KEY ("start_station_id") REFERENCES "dim_station" ("station_id");

ALTER TABLE "fact_trip" ADD FOREIGN KEY ("end_station_id") REFERENCES "dim_station" ("station_id");
