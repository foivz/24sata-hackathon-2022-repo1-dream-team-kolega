package com.example.financije;

import static java.lang.Integer.parseInt;

import com.opencsv.CSVReader;

import java.io.FileReader;
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

    private void initData()
    {
        allProdukt.add(new Baza("https://i.stack.imgur.com/SNKGt.png", "Lopov", "17.99", "internet", "wifi", 5000));

        try {

            // Create an object of filereader
            // class with CSV file as a parameter.
            FileReader filereader = new FileReader("C:\\Users\\Rikard\\Documents\\GitHub\\24sata-hackathon-2022-repo1-dream-team-kolega\\database2.csv");

            // create csvReader object passing
            // file reader as a parameter
            CSVReader csvReader = new CSVReader(filereader);
            String[] nextRecord;

            // we are going to read data line by line
            while ((nextRecord = csvReader.readNext()) != null) {
                for (String cell : nextRecord) {
                    String[] middleman = cell.split("\",\"");
                    allProdukt.add(new Baza(middleman[0], middleman[1], middleman[2], middleman[3], middleman[4], parseInt(middleman[5])));

                }

            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static synchronized Utils getInstance() {
        if (null == instance) {
            instance = new Utils();
        }
        return instance;
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
