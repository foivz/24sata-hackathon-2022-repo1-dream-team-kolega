package com.example.financije;

import static com.example.financije.Utils.allProdukt;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;

public class shoppingActivity extends AppCompatActivity {

    private TextView searchBox;

    ArrayList<Baza> pokazi = Utils.getPokazi();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shopping);

        ShoppingViewAdapter adapter = new ShoppingViewAdapter(this);
        RecyclerView shoopingRec = findViewById(R.id.shoopingRec);

        shoopingRec.setAdapter(adapter);
        shoopingRec.setLayoutManager(new GridLayoutManager(this,2));

        searchBox = findViewById(R.id.pretraga);

        Button btmSearch = findViewById(R.id.searchBtn);
        btmSearch.setOnClickListener(view -> {
            CharSequence user_in_char = searchBox.getText();
            String user_in = user_in_char.toString();
            int i;
            for (i = 0; i < allProdukt.size(); i++){
                if(allProdukt.get(i).getName().contains(user_in)){
                    pokazi.add(allProdukt.get(i));
                }
            }


        });

        if(pokazi != null) {
            adapter.setProdukt(Utils.getInstance().getAllProdukt());
        }else{
            adapter.setProdukt(Utils.getInstance().getPokazi());
            pokazi = null;
        }


    }
}