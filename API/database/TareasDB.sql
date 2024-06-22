--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

-- Started on 2024-06-22 17:28:02

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 16771)
-- Name: Tareas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Tareas" (
    "Id_Tarea" integer NOT NULL,
    "Nombre" character varying,
    "Descripcion" text,
    "Fecha_max" date
);


ALTER TABLE public."Tareas" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16770)
-- Name: Tareas_Id_Tarea_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Tareas" ALTER COLUMN "Id_Tarea" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Tareas_Id_Tarea_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4834 (class 0 OID 16771)
-- Dependencies: 216
-- Data for Name: Tareas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Tareas" ("Id_Tarea", "Nombre", "Descripcion", "Fecha_max") FROM stdin;
1	Responder preguntas	Responder las preguntas de la primera serie del examen	2024-07-01
2	Desarrollar API en Flask	Hacer una api para un to-do list en la segunda serie del examen	2024-07-05
3	Desarrollar un formulario en REact	Desarrollar un cliente React con Vite con un formulario	2024-07-10
\.


--
-- TOC entry 4840 (class 0 OID 0)
-- Dependencies: 215
-- Name: Tareas_Id_Tarea_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Tareas_Id_Tarea_seq"', 3, true);


--
-- TOC entry 4689 (class 2606 OID 16777)
-- Name: Tareas Tareas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Tareas"
    ADD CONSTRAINT "Tareas_pkey" PRIMARY KEY ("Id_Tarea");


-- Completed on 2024-06-22 17:28:02

--
-- PostgreSQL database dump complete
--

