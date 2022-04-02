package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;

import java.util.ArrayList;

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

                    handleAlreadyRead(incomingProdukt);
                }
            }
        }
    }

    private void handleAlreadyRead(final Baza produkt) {
        ArrayList<Baza> shoppingCart = Utils.getInstance().getShoppingList();

        boolean existInShopCart = false;

        for (Baza b: shoppingCart){
            if (b.getId() == produkt.getId()){
                existInShopCart = true;
            }
        }
        if (existInShopCart){
            btnAddFavorite.setEnabled(false);
        }else {
            btnAddFavorite.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (Utils.getInstance().addToShopCart(produkt)){
                        Toast.makeText(ProduktActivity.this, "Dodano u shopping cart", Toast.LENGTH_SHORT).show();


                        Intent intent = new Intent(ProduktActivity.this, ShoppingListActivity.class);
                        startActivity(intent);
                    }
                    else{
                        Toast.makeText(ProduktActivity.this, "Ode sve kvragu", Toast.LENGTH_SHORT).show();
                    }
                }
            });
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