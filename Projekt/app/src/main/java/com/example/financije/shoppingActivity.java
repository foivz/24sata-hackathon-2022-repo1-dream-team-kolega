package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;

import java.util.ArrayList;

public class shoppingActivity extends AppCompatActivity {

    private RecyclerView shoopingRec;
    private  ShoppingViewAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shopping);

        adapter = new ShoppingViewAdapter(this);
        shoopingRec = findViewById(R.id.shoopingRec);

        shoopingRec.setAdapter(adapter);
        shoopingRec.setLayoutManager(new GridLayoutManager(this,2));

        ArrayList<Baza> produkt = new ArrayList<>();
        produkt.add(new Baza("kobasa","50","https://ferbezar.com/wp-content/uploads/2016/11/slavonska-kobasica1.jpg"));
        produkt.add(new Baza("Hren","20","https://podravkaiovariations.azureedge.net/05aa6e54-8f62-11ea-916b-fefaf5a5a600/v/9ed607bc-4c1b-11ea-9bb0-92f307bc0925/450x600-9ed6ed4e-4c1b-11ea-9140-92f307bc0925.png"));
        produkt.add(new Baza("Paradajs","10","https://alternativa-za-vas.com/images/uploads/paradajz3.jpg"));

        adapter.setProdukt(produkt);
    }
}