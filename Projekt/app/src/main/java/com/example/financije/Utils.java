package com.example.financije;

import java.util.ArrayList;

public class Utils {
    private static Utils instance;
    private static ArrayList<Baza> allProdukt;
    private static ArrayList<Baza> shoppingList;

    private Utils(){
        if(null == allProdukt){
            allProdukt = new ArrayList<>();
            initData();
        }
        if(null == shoppingList){
            shoppingList = new ArrayList<>();
        }
    }

    private void initData() {
        //TODO: add initial data
        allProdukt.add(new Baza("kobasa","50 kn","https://ferbezar.com/wp-content/uploads/2016/11/slavonska-kobasica1.jpg",1));
        allProdukt.add(new Baza("Hren","20 kn","https://podravkaiovariations.azureedge.net/05aa6e54-8f62-11ea-916b-fefaf5a5a600/v/9ed607bc-4c1b-11ea-9bb0-92f307bc0925/450x600-9ed6ed4e-4c1b-11ea-9140-92f307bc0925.png",2));
        allProdukt.add(new Baza("Paradajs","10 kn","https://alternativa-za-vas.com/images/uploads/paradajz3.jpg",3));

    }

    public static synchronized Utils getInstance() {
        if (null != instance){
            return instance;
        }else{
            instance = new Utils();
            return instance;
        }
    }

    public static ArrayList<Baza> getAllProdukt() {
        return allProdukt;
    }

    public static ArrayList<Baza> getShoppingList() {
        return shoppingList;
    }

    public Baza getProduktByID(int id){
        for (Baza b: allProdukt){
            if (b.getId() == id){
                return b;
            }
        }
        return null;
    }
}
