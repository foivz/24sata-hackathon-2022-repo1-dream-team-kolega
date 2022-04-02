package com.example.financije;

public class Baza {
    private int id;
    private String name;
    private String price;
    private String link;


    public Baza(String name, String price, String link, int id) {
        this.name = name;
        this.price = price;
        this.link = link;
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

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
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
