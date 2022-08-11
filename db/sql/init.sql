CREATE TABLE "posts" IF NOT EXISTS (
  "id" SERIAL PRIMARY KEY,
  "title" varchar NOT NULL,
  "content" varchar NOT NULL,
  "published" boolean NOT NULL,
  "published_at" timestamp NOT NULL
);

CREATE TABLE "users" IF NOT EXISTS (
  "id" SERIAL PRIMARY KEY,
  "username" varchar NOT NULL,
  "created_at" datetime DEFAULT (now())
);

ALTER TABLE "posts" ADD FOREIGN KEY ("id") REFERENCES "users" ("id") IF NOT EXISTS;
