package com.example.financije;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

import androidx.appcompat.app.AppCompatActivity;

public class LoadingActivity extends AppCompatActivity {

    boolean isLogedIn=true;//TODO:Nesto bolje od ovog
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);
        Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            public void run() {
                Stvar();
            }
        }, 1000);

    }
    public void Stvar(){

        Intent intent;
        if (isLogedIn==false) intent=new Intent(LoadingActivity.this,LoginActivity.class);
        else intent=new Intent(LoadingActivity.this,FamilyActivity.class);
        startActivity(intent);
    }
}