package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import android.util.Log;
import android.util.Log;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.lang.reflect.Type;
import java.util.List;
import java.lang.reflect.Type;
import java.util.List;
import android.os.Bundle;
import android.widget.Toast;

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

        adapter.setProdukt(produkt);
    }
}