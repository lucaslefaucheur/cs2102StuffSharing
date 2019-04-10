BEGIN;
--
-- Create model LoanProposition
--
CREATE TABLE "stuffsharing_loanproposition" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "start_date" date NOT NULL, "end_date" date NOT NULL, "price" real NOT NULL, "pickupAdress" varchar(1000) NOT NULL, "returnAdress" varchar(1000) NOT NULL, "available" bool NOT NULL);
--
-- Create model LoanRequest
--
CREATE TABLE "stuffsharing_loanrequest" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "accepted" bool NOT NULL, "price" real NOT NULL);
--
-- Create model Profile
--
CREATE TABLE "stuffsharing_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Name" varchar(255) NOT NULL, "phone" varchar(12) NOT NULL, "address" varchar(1000) NOT NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Stuff
--
CREATE TABLE "stuffsharing_stuff" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "description" varchar(255) NOT NULL, "tags" varchar(1000) NOT NULL, "image" varchar(1000) NOT NULL, "owner_id" integer NOT NULL REFERENCES "stuffsharing_profile" ("user_id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field borrower to loanrequest
--
ALTER TABLE "stuffsharing_loanrequest" RENAME TO "stuffsharing_loanrequest__old";
CREATE TABLE "stuffsharing_loanrequest" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "accepted" bool NOT NULL, "price" real NOT NULL, "borrower_id" integer NOT NULL REFERENCES "stuffsharing_profile" ("user_id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "stuffsharing_loanrequest" ("id", "accepted", "price", "borrower_id") SELECT "id", "accepted", "price", NULL FROM "stuffsharing_loanrequest__old";
DROP TABLE "stuffsharing_loanrequest__old";
CREATE INDEX "stuffsharing_stuff_owner_id_5c0ad3fb" ON "stuffsharing_stuff" ("owner_id");
CREATE INDEX "stuffsharing_loanrequest_borrower_id_2527dde9" ON "stuffsharing_loanrequest" ("borrower_id");
--
-- Add field original_Proposition to loanrequest
--
ALTER TABLE "stuffsharing_loanrequest" RENAME TO "stuffsharing_loanrequest__old";
CREATE TABLE "stuffsharing_loanrequest" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "accepted" bool NOT NULL, "price" real NOT NULL, "borrower_id" integer NOT NULL REFERENCES "stuffsharing_profile" ("user_id") DEFERRABLE INITIALLY DEFERRED, "original_Proposition_id" integer NOT NULL REFERENCES "stuffsharing_loanproposition" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "stuffsharing_loanrequest" ("id", "accepted", "price", "borrower_id", "original_Proposition_id") SELECT "id", "accepted", "price", "borrower_id", NULL FROM "stuffsharing_loanrequest__old";
DROP TABLE "stuffsharing_loanrequest__old";
CREATE INDEX "stuffsharing_loanrequest_borrower_id_2527dde9" ON "stuffsharing_loanrequest" ("borrower_id");
CREATE INDEX "stuffsharing_loanrequest_original_Proposition_id_3b066dd3" ON "stuffsharing_loanrequest" ("original_Proposition_id");
--
-- Add field owner to loanproposition
--
ALTER TABLE "stuffsharing_loanproposition" RENAME TO "stuffsharing_loanproposition__old";
CREATE TABLE "stuffsharing_loanproposition" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "start_date" date NOT NULL, "end_date" date NOT NULL, "price" real NOT NULL, "pickupAdress" varchar(1000) NOT NULL, "returnAdress" varchar(1000) NOT NULL, "available" bool NOT NULL, "owner_id" integer NOT NULL REFERENCES "stuffsharing_profile" ("user_id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "stuffsharing_loanproposition" ("id", "start_date", "end_date", "price", "pickupAdress", "returnAdress", "available", "owner_id") SELECT "id", "start_date", "end_date", "price", "pickupAdress", "returnAdress", "available", NULL FROM "stuffsharing_loanproposition__old";
DROP TABLE "stuffsharing_loanproposition__old";
CREATE INDEX "stuffsharing_loanproposition_owner_id_ff556d70" ON "stuffsharing_loanproposition" ("owner_id");
--
-- Add field stuff_for_lown to loanproposition
--
ALTER TABLE "stuffsharing_loanproposition" RENAME TO "stuffsharing_loanproposition__old";
CREATE TABLE "stuffsharing_loanproposition" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "start_date" date NOT NULL, "end_date" date NOT NULL, "price" real NOT NULL, "pickupAdress" varchar(1000) NOT NULL, "returnAdress" varchar(1000) NOT NULL, "available" bool NOT NULL, "owner_id" integer NOT NULL REFERENCES "stuffsharing_profile" ("user_id") DEFERRABLE INITIALLY DEFERRED, "stuff_for_lown_id" integer NOT NULL REFERENCES "stuffsharing_stuff" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "stuffsharing_loanproposition" ("id", "start_date", "end_date", "price", "pickupAdress", "returnAdress", "available", "owner_id", "stuff_for_lown_id") SELECT "id", "start_date", "end_date", "price", "pickupAdress", "returnAdress", "available", "owner_id", NULL FROM "stuffsharing_loanproposition__old";
DROP TABLE "stuffsharing_loanproposition__old";
CREATE INDEX "stuffsharing_loanproposition_owner_id_ff556d70" ON "stuffsharing_loanproposition" ("owner_id");
CREATE INDEX "stuffsharing_loanproposition_stuff_for_lown_id_f58a4f88" ON "stuffsharing_loanproposition" ("stuff_for_lown_id");
COMMIT;
