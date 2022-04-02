package com.example.financije;

public class Baza {
    private String name;
    private String price;
    private String link;
    private String tag;
    private String ducan;

    public void setTag(String tag) {
        this.tag = tag;
    }

    public void setDucan(String ducan) {
        this.ducan = ducan;
    }

    public String getTag() {
        return tag;
    }

    public String getDucan() {
        return ducan;
    }

    public Baza(String name, String price, String link, String tag, String ducan) {
        this.name = name;
        this.price = price;
        this.link = link;
        this.tag = tag;
        this.ducan = ducan;
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
