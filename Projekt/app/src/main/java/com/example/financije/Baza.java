package com.example.financije;

public class Baza {
    private int id;
    private String name;
    private String store;
    private String tag;
    private Double price;
    private String link;


    public Baza(String link, String name, Double price, String store, String tag, int id) {
        this.link = link;
        this.name = name;
        this.price = price;
        this.store = store;
        this.tag = tag;
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    @Override
    public String toString() {
        return "Baza{" +
                "name='" + name + '\'' +
                ", price=" + price +
                ", link='" + link + '\'' +
                '}';
    }
}
