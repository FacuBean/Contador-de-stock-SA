create  table Products (ID serial primary key not null, "name" varchar(100) , color varchar(50), description varchar(300), price float, stock int, upload_date DATE, update_item_date DATE, date_restock DATE, items_sold int);

-- Table: public.products

-- DROP TABLE IF EXISTS public.products;

CREATE TABLE IF NOT EXISTS public.products
(
    id integer NOT NULL DEFAULT nextval('products_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default",
    color character varying(50) COLLATE pg_catalog."default",
    description character varying(300) COLLATE pg_catalog."default",
    price double precision,
    stock integer,
    upload_date date,
    update_item_date date,
    date_restock date,
    items_sold integer,
    category_color character varying(60) COLLATE pg_catalog."default",
    color_code character varying(6) COLLATE pg_catalog."default",
    CONSTRAINT products_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.products
    OWNER to postgres;