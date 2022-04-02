package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button shoppingBtn, troskoviBtn, predictionBtn, helpBtn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();
        shoppingBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, shoppingActivity.class);
                startActivity(intent);
            }
        });

        troskoviBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, AnalizaActivity.class);
                startActivity(intent);
            }
        });

        predictionBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, TroskoviActivity.class);
                startActivity(intent);
            }
        });
    }

    private void initViews(){
        shoppingBtn = findViewById(R.id.shoppingBtn);
        troskoviBtn = findViewById(R.id.troskoviBtn);
        predictionBtn = findViewById(R.id.predictionBtn);

    }
}

