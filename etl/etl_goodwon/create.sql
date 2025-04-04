-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create sample table
CREATE TABLE tb_youtube (
    id SERIAL primary key,
    inventory VARCHAR(500) not null,
    title VARCHAR(500) not null,
    youtube_info JSONB not null,
    embedding_ollama vector(768) 
);

-- Create comment 
comment on table tb_youtube is '유튜브 테이블';
comment on column tb_youtube.id is '아이디';
comment on column tb_youtube.inventory is '목록';
comment on column tb_youtube.title is '영상 제목';
comment on column tb_youtube.youtube_info is '영상 정보';
comment on column tb_youtube.embedding_ollama is '벡터 데이터';
