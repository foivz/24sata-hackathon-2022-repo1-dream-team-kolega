package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class ProduktActivity extends AppCompatActivity {
    public static  final String PRODUKT_ID_KEY = "produktId";

    private ImageView imgProdukt;
    private TextView txtNameProdukt, txtCijenaProdukt;
    private Button btnAddFavorite;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_produkt);

        initViews();

        Intent intent = getIntent();
        if (null != intent){
            int produktId = intent.getIntExtra(PRODUKT_ID_KEY,-1);
            if (produktId != -1){
                Baza incomingProdukt = Utils.getInstance().getProduktByID(produktId);
                if (null != incomingProdukt){
                    setData(incomingProdukt);
                }
            }
        }
    }

    private void setData(Baza produkt){
        txtNameProdukt.setText(produkt.getName());
        txtCijenaProdukt.setText(produkt.getPrice());
        Glide.with(this)
                .asBitmap().load(produkt.getLink())
                .into(imgProdukt);

    }

    private void initViews(){
        imgProdukt = findViewById(R.id.produktImg);
        txtNameProdukt = findViewById(R.id.txtNameProdukt);
        txtCijenaProdukt = findViewById(R.id.txtCijenaProdukt);
        btnAddFavorite = findViewById(R.id.addFavorite);
    }
}